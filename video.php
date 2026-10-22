<?php
// Prevent PHP execution time limit for long video streaming
@set_time_limit(0);

$id = isset($_GET['id']) ? trim($_GET['id']) : '';
if (empty($id) || !preg_match('/^[a-zA-Z0-9_-]+$/', $id)) {
    http_response_code(400);
    header('Content-Type: text/plain');
    echo "Invalid or missing video ID";
    exit;
}

$driveUrl = "https://drive.usercontent.google.com/download?id=" . $id . "&export=download&confirm=t";

// Setup cURL to stream video from Google Drive
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $driveUrl);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_AUTOREFERER, true);
curl_setopt($ch, CURLOPT_MAXREDIRS, 5);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 15);
curl_setopt($ch, CURLOPT_TIMEOUT, 0); // No timeout for streaming

// Forward Request Headers (crucial for video scrubbing & byte ranges)
$reqHeaders = [
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
];

if (isset($_SERVER['HTTP_RANGE'])) {
    $reqHeaders[] = 'Range: ' . $_SERVER['HTTP_RANGE'];
}

curl_setopt($ch, CURLOPT_HTTPHEADER, $reqHeaders);

// Disable output buffering
while (ob_get_level()) {
    ob_end_clean();
}

// Forward relevant streaming headers from Google Drive
curl_setopt($ch, CURLOPT_HEADERFUNCTION, function($curl, $headerLine) {
    $len = strlen($headerLine);
    $trimmed = trim($headerLine);
    if (empty($trimmed)) return $len;

    $lower = strtolower($trimmed);

    // Forward HTTP status code (200, 206 Partial Content, etc.)
    if (strpos($lower, 'http/') === 0) {
        $parts = explode(' ', $trimmed, 3);
        if (isset($parts[1])) {
            http_response_code((int)$parts[1]);
        }
        return $len;
    }

    // Forward essential video streaming headers
    $allowed = ['content-type', 'content-range', 'accept-ranges', 'content-length', 'last-modified', 'etag'];
    foreach ($allowed as $prefix) {
        if (strpos($lower, $prefix . ':') === 0) {
            header($trimmed);
            break;
        }
    }

    return $len;
});

// Video headers for browser inline playback & CORS
header('Content-Disposition: inline');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Headers: Range, Content-Type');
header('Access-Control-Expose-Headers: Content-Range, Content-Length, Accept-Ranges');
header('Cache-Control: public, max-age=86400');

// Stream directly to browser
curl_setopt($ch, CURLOPT_RETURNTRANSFER, false);
curl_setopt($ch, CURLOPT_WRITEFUNCTION, function($curl, $data) {
    echo $data;
    @flush();
    return strlen($data);
});

// Execute stream
curl_exec($ch);
curl_close($ch);
exit;
