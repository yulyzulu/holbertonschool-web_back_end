const app = require('http');

app.createServer((req, res) => {
  res.end('Hello Holberton School!');
}).listen(1245);
