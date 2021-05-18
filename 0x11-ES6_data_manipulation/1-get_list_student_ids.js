export default function getListStudentIds(getList) {
  const array = [];
  if (!Array.isArray(getList)) {
    return array;
  }

  getList.map(item => array.push(item.id));
  return array;
}
