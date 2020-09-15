#!/usr/bin/node
const nan = isNaN(process.argv[2]);
if (nan === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) { console.log('X'.repeat(process.argv[2])); }
}
