process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', function() {
  const name = String(process.stdin.read());
  showName(name);
})

const showName = (name) => {
  if (name)
    console.log('Your name is: ' + name);
}
const laFinale = () => {
  if (process.stdout.isTTY)
    process.stdout.write('This important software is now closing\n');
}
