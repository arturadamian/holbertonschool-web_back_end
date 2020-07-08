export default function getStudentsByLocation(array, city) {
  return array.filter((item) => { if (item.location === city) item });
}
