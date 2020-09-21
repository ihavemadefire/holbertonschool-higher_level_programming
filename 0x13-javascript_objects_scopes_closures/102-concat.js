#!/usr/bin/node
const args = (process.argv);
const fs = require('fs');
const one = fs.readFileSync(args[2]);
const two = fs.readFileSync(args[3]);
fs.writeFileSync(args[4], one + two);
