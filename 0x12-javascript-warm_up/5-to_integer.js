#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (!isNaN(number)) {
  console.log(`My number is: ${number}`);
} else {
  console.log('Not a number');
}
