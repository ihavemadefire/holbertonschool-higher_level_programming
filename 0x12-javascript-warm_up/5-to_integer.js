#!/usr/bin/node
const nan = isNaN(process.argv[2]);
if (nan === true) {
  console.log('Not a number');
} else {
  console.log('My Number : ' + process.argv[2]);
}
