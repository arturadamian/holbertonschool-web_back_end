export default function guardrail(mathFunction) {
  let queue = []
  try {
    const val = mathFunction();
    queue.push(val);
  } catch (error) {
    queue.push(error);
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}