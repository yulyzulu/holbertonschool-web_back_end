export default function appendToEachArrayValue(array, appendString) {
  let i = 0;
  for (let idx of array) {
    array[i] = appendString + idx;
    i++;
  }

  return array
}
