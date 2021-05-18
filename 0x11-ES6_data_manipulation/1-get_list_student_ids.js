export default function getListStudentIds(getList) {
  const array = [];
  if (!Array.isArray(getList) && getList.every(i => typeof i !== 'object')) {
    return array;
  }

  getList.map(item => array.push(item.id));
  return array;
}
