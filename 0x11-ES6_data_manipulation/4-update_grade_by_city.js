export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  return getListStudents.filter((item) => item.location === city)
    .map((item) => {
      const grades = newGrades
        .filter((grade) => grade.studentId === item.id)
        .map((i) => i.grade)[0];
      const grade = grades || 'N/A';
      return { ...item, grade };
    });
}
