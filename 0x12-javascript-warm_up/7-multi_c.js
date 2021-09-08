#!/usr/bin/node
const number = Math.floor(Number(process.argv[2]));
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < number; index++) {
    console.log('C is fun');
  }
}
