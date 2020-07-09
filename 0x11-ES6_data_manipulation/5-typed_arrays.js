export default function createInt8TypedArray(length, position, value) {
  if (position > length) throw new Error('Position outside range');
let buffer = new ArrayBuffer(length);const int8BufferArray = new Int8Array(buffer, position, value);
}