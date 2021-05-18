export default function getListStudentIds(getListStudents) {
  if (!Array.isArray(getListStudents) || getListStudents.every(i => typeof i !== 'object')) {
    return [];
  }

  return getListStudents.map((item) => item.id);
}
