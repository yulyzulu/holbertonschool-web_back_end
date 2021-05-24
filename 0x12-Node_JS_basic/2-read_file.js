const fs = require('fs');

function countStudents(path) {
  try {
    let students = fs.readFileSync(path).toString().split('\n');
    students = students.slice(1, students.length - 1);
    console.log(`Number of students: ${students.length}`);

    const studentDescription = {};
    for (const i of students) {
      const student = i.split(',');
      if (!studentDescription[student[3]]) {
        studentDescription[student[3]] = [];
      }
      studentDescription[student[3]].push(student[0]);
    }
    for (const item in studentDescription) {
      if (item) {
        console.log(`Number of students in ${item}: ${studentDescription[item].length}. List: ${studentDescription[item].join(', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
