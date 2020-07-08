export default function getListStudentIds(array) {
  if (!array) return [];
  return array.map((item) => item.id);
}
