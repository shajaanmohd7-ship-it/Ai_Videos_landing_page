import http.server
import socketserver
import urllib.parse
import urllib.request
import os
import sys
import shutil

PORT = 5173

class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_HEAD(self):
        if self.path.startswith('/video') or self.path.startswith('/api/video'):
            self.handle_video(head_only=True)
        else:
            super().do_HEAD()

    def do_GET(self):
        if self.path.startswith('/video') or self.path.startswith('/api/video'):
            self.handle_video(head_only=False)
        else:
            super().do_GET()

    def handle_video(self, head_only=False):
        parsed = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed.query)
        video_id = query.get('id', [None])[0]

        if not video_id:
            self.send_error(400, "Missing 'id' parameter")
            return

        drive_url = f"https://drive.usercontent.google.com/download?id={video_id}&export=download&confirm=t"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }

        # Forward Range header for video seeking & partial content
        if 'Range' in self.headers:
            headers['Range'] = self.headers['Range']

        req = urllib.request.Request(drive_url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as upstream:
                self.send_response(upstream.status)

                # Send required headers for video streaming
                for h in ['Content-Type', 'Content-Range', 'Accept-Ranges', 'Content-Length']:
                    val = upstream.headers.get(h)
                    if val:
                        self.send_header(h, val)

                # Ensure inline playback (not attachment) & CORS
                self.send_header('Content-Disposition', 'inline')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Cache-Control', 'public, max-age=3600')
                self.end_headers()

                if not head_only:
                    try:
                        shutil.copyfileobj(upstream, self.wfile, length=64 * 1024)
                    except (BrokenPipeError, ConnectionResetError):
                        # Client stopped video or navigated away
                        pass
        except urllib.error.HTTPError as e:
            self.send_error(e.code, str(e.reason))
        except Exception as e:
            self.send_error(500, str(e))

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    print(f"Starting Threaded Video Server on 0.0.0.0:{PORT}...")
    with ThreadingHTTPServer(('0.0.0.0', PORT), CustomRequestHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        httpd.serve_forever()
