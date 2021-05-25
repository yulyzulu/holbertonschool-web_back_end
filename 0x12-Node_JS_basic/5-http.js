const http = require('http');

const args = process.argv.slice(2);
const countStudents = require('./3-read_file_async');

const DATABASE = args[0];

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.write('Hello Holberton School!');
    res.end()
  }
  if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const students = await countStudents(DATABASE);
      res.write(`${students.join('\n')}`);
      res.end();
    } catch (err) {
      res.write(err.message);
    }
  }
  res.end();
});

app.listen(port, hostname, () => {
});

module.exports = app;
