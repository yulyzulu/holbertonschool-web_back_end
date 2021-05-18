export default function getStudentIdsSum(getListStudents) {
  if (!Array.isArray(getListStudents)) {
    return [];
  }
  return getListStudents.reduce((a, b) => a + b.id, 0);
}
