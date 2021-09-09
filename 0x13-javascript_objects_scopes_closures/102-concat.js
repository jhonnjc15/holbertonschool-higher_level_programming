#!/usr/bin/node
const fs = require('fs');
const d1 = fs.readFileSync(process.argv[2], 'utf8');
const d2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], d1 + d2);
