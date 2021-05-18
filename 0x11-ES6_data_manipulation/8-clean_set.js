export default function cleanSet(set, startString) {
  let string = '';
  if (!startString || !startString.length) {
    return string;
  }
  for (let item of set) {
    if (item && item.startsWith(startString)) {
      string += `${item.slice(startString.length)}-`;
    }
  }
  return string.slice(0, string.length - 1);
}
