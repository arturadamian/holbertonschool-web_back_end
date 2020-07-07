class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== String) throw TypeError('name must be a String');
    if (typeof(length) !== Number) throw TypeError('length must be a Number');
    if (students.constructor !== Array || students.every((el) => typeof el === 'string')) {
      throw TypeError('students must be an Array of Strings');
    };
    this._name = name;
    this._length = length;
    this._students = students;
  }
  get name() {
    return this._name
  }

  get length() {
    return this._length
  }

  get students() {
    return this._students
  }

  set name(newName) {
    this._name = newName;
  }

  set length(newLength) {
    this._length = newLength;
  }

  set students(newStudents) {
    this._students = newStudents;
  }
}
