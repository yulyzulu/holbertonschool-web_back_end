export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  const array = getListStudents.filter((item) => item.location === city).map((item, index) => {
    const grades = newGrades.filter((grade) => grade.studentId === item.id);
    if (!grades.length){
      item.grade = 'N/A';
    } else {
      item.grade = grades[0].grade;
    }
    return item;
  });
  return array;
}
