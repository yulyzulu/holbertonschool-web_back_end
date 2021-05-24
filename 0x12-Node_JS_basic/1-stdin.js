process.stdin.resume();
console.log('Welcome to Holberton School, what is your name?');
process.stdin.on('readable', function() {
  const name = process.stdin.read();
  if (name !== null) {
    process.stdout.write(`Your name is: ${name}`);
  }
});

process.stdin.on('end', function() {
  process.stdout.write('This important software is now closing\n');
});
