export default function cleanSet(set, startString) {
  let resultString = '';
  set.forEach((el) => {
    if (el.startsWith(startString)) {
      const word = el.slice(startString.length);
    } else { continue; };
    resultString += `${word}-`;
  });
  return resultString.slice(0, resultString.length - 1);
}
