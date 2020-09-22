#!/usr/bin/node
const args = (process.argv);
const fs = require('fs');
const one = args[3];
fs.writeFileSync(args[2], one, 'utf-8');
