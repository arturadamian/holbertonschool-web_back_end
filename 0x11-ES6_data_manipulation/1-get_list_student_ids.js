export default function getListStudentIds(array) {
  if (typeof array !== Array.isArray) return [];
  return array.map((item) => item.id);
}
