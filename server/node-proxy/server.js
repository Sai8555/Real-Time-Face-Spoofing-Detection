const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();
const PORT = 3000; // Port for the Node.js server
const FLASK_PORT = 5000; // Port where Flask app is running

// Serve static files (optional)
app.use(express.static('public'));

// Proxy requests to Flask app
app.use(
  '/',
  createProxyMiddleware({
    target: `http://localhost:${FLASK_PORT}`,
    changeOrigin: true,
    ws: true, // Enable WebSocket support if needed
  })
);

// Start the Node.js server
// app.listen(PORT, () => {
//   console.log(`Node.js server running on http://localhost:${PORT}`);
// });
app.listen(PORT, '0.0.0.0', () => {
    console.log(`Node.js server running on http://0.0.0.0:${PORT}`);
  });