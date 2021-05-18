export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw new TypeError('Name must be a string');
    if (typeof length !== 'number') throw new TypeError('Length must be a number');
    if (!Array.isArray(students) && students.every(i => typeof i !== 'string')) throw new TypeError('Students must be an array of Strings');

    this._name = name;
    this._length = length;
    this._students = students;
  }

  set name(name) {
    if (typeof name !== 'string') throw new TypeError('Name must be a string');
    this._name = name;
  }

  get name() {
    return this._name;
  }

  set length(length) {
    if (typeof length !== 'number') throw new TypeError('number');
    this._length = length;
  }

  get length() {
    return this._length;
  }

  set students(students) {
    if (!students.isArray && students.every(i => typeof i !== 'string')) throw new TypeError('Students must be an array of Strings');
    this._students = students;
  }

  get students() {
    return this._students;
  }
}
