#!/usr/bin/node
console.log(fact(parseInt(process.argv[2], 10)));
function fact (n) {
  if (n === 0 || n === 1 || isNaN(n)) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
