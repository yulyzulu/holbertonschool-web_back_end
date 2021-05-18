export default function getListStudentIds(getListStudents) {
  const array = [];
  if (!Array.isArray(getListStudents) || getListStudents.every(i => typeof i !== 'object')) {
    return array;
  }

  getListStudents.map(item => {
    array.push(item.id)
  });
  return array;
}
