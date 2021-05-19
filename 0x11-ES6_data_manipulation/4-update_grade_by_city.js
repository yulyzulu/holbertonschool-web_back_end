export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  const array = getListStudents.filter((item) => item.location === city).map((item) => {
    const grades = newGrades.filter((grade) => grade.studentId === item.id, );
    let grade;
    if (!grades.length) {
      grade = 'N/A';
    } else {
      grade = grades[0].grade;
    }
    return { ...item, grade };
  });
  return array;
}
