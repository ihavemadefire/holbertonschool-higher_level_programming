#!/usr/bin/node
const args = (process.argv);
const fs = require('fs');
fs.readFile(args[2], 'utf-8', function (error, content) {
  console.log(content || error);
});
