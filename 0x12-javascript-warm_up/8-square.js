#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
}
let i;
let j;
for (i = 0; i < size; i++) {
  let row = '';
  for (j = 0; j < size; j++) {
    row = row + 'X';
  }
  console.log(row);
}
