export default function appendToEachArrayValue(array, appendString) {
  const array1 = [];
  for (const idx of array) {
    array1.push(appendString + idx)
  }

  return array1
}
