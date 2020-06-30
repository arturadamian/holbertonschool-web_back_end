export default function iterateThroughObject(reportWithIterator) {
  let x = reportWithIterator.next();
  let res = '';
  while (!x.done) {
    res += `${x.value} | `;
    x = reportWithIterator.next();
  }
  return res.slice(0, res.length - 3);
}
