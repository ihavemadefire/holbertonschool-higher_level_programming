#!/usr/bin/node
const dict = require('./101-data.js').dict;
const ret = {};
for (const k in dict) {
  // first time to create that key
  if (ret[dict[k]] === undefined) {
    ret[dict[k]] = [k];
  } else {
    // push it to the existing key
    ret[dict[k]].push(k);
  }
}
console.log(ret);
