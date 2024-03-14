#!/usr/bin/node
if (!isNaN(process.argv[2])) {
  const len = Math.floor(Number(process.argv[2]));
  const str = 'X';
  for (let i = 0; i < len; i += 1) {
    console.log(str.repeat(len));
  }
} else {
  console.log('Missing size');
}
