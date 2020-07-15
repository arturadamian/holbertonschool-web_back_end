const showName = (name) => {
  if (name) console.log(`Your name is: ${name}`);
};

process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  const name = String(process.stdin.read());
  showName(name);
});

process.stdin.on('end', () => {
  if (process.stdout.isTTY) process.stdout.write('This important software is now closing\n');
});