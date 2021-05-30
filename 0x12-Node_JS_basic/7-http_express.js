const express = require('express');

const countStudents = require('./3-read_file_async');
const args = process.argv.slice(2);

const database = args[0];

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const text = 'This is the list of our students\n';
  try {
    const students = await countStudents(database);
    res.send(`${text}${students.join('\n')}`);
  } catch (err) {
    res.send(`${text}${err.message}`);
  }
});

app.listen(1245, () => {
  console.log(`Server running at: http://localhost:${PORT}/`);
});

module.exports = app;
