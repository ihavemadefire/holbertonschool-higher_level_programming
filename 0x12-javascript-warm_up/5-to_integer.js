#!/usr/bin/node
const nan = isNaN(process.argv[2]);
if (nan === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2], 10));
}
