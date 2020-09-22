#!/usr/bin/node
const args = (process.argv);
const fs = require('fs');
const one = args[3];
fs.writeFile(args[2], one, 'utf8', error => { if (error) console.log(error); });
