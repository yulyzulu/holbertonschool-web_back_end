const fs = require('fs');

function countStudents(path) {
  const promise = (resolve, reject) => {
    fs.readFile(path, (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      }
      if (data) {
        let students = data.toString().split('\n');
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
      }
      resolve();
    });
  };
  return new Promise(promise);
}

module.exports = countStudents;
