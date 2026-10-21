const https = require('https');
const http = require('http');

function streamVideo(url, reqHeaders, res, redirectCount = 0) {
  if (redirectCount > 5) {
    return res.status(500).send('Too many redirects');
  }

  const client = url.startsWith('https') ? https : http;
  const headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  };

  if (reqHeaders.range) {
    headers['range'] = reqHeaders.range;
  }

  client.get(url, { headers }, (upstream) => {
    // Follow redirect if 301, 302, 307, 308
    if (upstream.statusCode >= 300 && upstream.statusCode < 400 && upstream.headers.location) {
      return streamVideo(upstream.headers.location, reqHeaders, res, redirectCount + 1);
    }

    res.status(upstream.statusCode);

    const copyHeaders = ['content-type', 'content-range', 'accept-ranges', 'content-length'];
    for (const h of copyHeaders) {
      if (upstream.headers[h]) {
        res.setHeader(h, upstream.headers[h]);
      }
    }

    res.setHeader('Content-Disposition', 'inline');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Cache-Control', 'public, max-age=3600');

    upstream.pipe(res);
  }).on('error', (err) => {
    res.status(500).send(err.message);
  });
}

module.exports = function handler(req, res) {
  const { id } = req.query;
  if (!id) {
    return res.status(400).send('Missing video id');
  }

  const driveUrl = `https://drive.usercontent.google.com/download?id=${id}&export=download&confirm=t`;
  streamVideo(driveUrl, req.headers, res);
};
