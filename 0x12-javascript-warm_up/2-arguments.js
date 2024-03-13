#!/usr/bin/node

const process = require('process');
if (process.argv[2] != undefined) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
