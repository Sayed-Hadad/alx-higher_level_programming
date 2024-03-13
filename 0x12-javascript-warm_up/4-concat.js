#!/usr/bin/node

const process = require('process');
if (process.argv[2] != null & process.argv[3] != null) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else if (process.argv[2] != null) {
  console.log(process.argv[2] + ' is ' + undefined);
} else if (process.argv[3] != null) {
  console.log(undefined + ' is ' + process.argv[2]);
} else {
  console.log(undefined + ' is ' + undefined);
}
