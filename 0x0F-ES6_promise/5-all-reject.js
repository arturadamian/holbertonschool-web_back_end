export default function uploadPhoto(fileName) {
  return new Promise.reject(new Error(`${fileName} cannot be processed`));
}
