#!/usr/bin/node
const nan1 = isNaN(process.argv[2]);
const nan2 = isNaN(process.argv[3]);
if (nan1 === true || nan2 === true) {
  console.log('NaN');
} else {
  const a = parseInt(process.argv[2], 10);
  const b = parseInt(process.argv[3], 10);
  console.log(add(a, b));
}
function add (a, b) {
  return a + b;
}
