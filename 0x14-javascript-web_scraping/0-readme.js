#!/usr/bin/node
const args = (process.argv);
const fs = require('fs');
const one = fs.readFileSync(args[2], 'utf-8');
console.log(one);
