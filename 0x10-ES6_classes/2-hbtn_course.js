export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('name must be a String');
    if (typeof length !== 'number') throw TypeError('length must be a Number');
    if (students.constructor !== Array || students.every((el) => typeof el === 'string')) {
      throw TypeError('students must be an Array of Strings');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    if (students.constructor !== Array || students.every((el) => typeof el === 'string')) {
      throw TypeError('students must be an Array of Strings');
    }
    return this._students;
  }

  set name(newName) {
    if (typeof name !== 'string') throw TypeError('name must be a String');
    this._name = newName;
  }

  set length(newLength) {
    if (typeof length !== 'number') throw TypeError('length must be a Number');
    this._length = newLength;
  }

  set students(newStudents) {
    this._students = newStudents;
  }
}
