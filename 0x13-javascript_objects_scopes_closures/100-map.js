#!/usr/bin/node
const init = require('./100-data').list;
console.log(init);
const newlist = init.map((x, y) => x * y);
console.log(newlist);
