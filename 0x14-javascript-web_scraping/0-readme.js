#!/usr/bin/node
const args = (process.argv);
const fs = require('fs');
fs.readFile(args[2], 'utf8', function (error, content) {
  console.log(error || content);
});
