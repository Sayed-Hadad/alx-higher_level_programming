#!/usr/bin/node

const size = process.argv[2];
if (!isNaN(size)) {
  for (let row = 0; row < size; row++) {
    let line = '';
    for (let col = 0; col < size; col++) {
      line += 'x';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
