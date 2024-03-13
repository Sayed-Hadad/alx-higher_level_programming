#!/usr/bin/node

const process = require('process');
if (process.argv[2] != null) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
