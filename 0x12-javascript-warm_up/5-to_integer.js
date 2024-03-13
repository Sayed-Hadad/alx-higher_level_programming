#!/usr/bin/node

const firstArg = process.argv[2];
const p = parseInt(firstArg);

if (!isNaN(p)) {
  console.log('My number: ' + p);
} else {
  console.log('Not a number');
}
