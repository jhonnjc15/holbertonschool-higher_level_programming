#!/usr/bin/node
const number = Math.floor(Number(process.argv[2]));
let message = 'Not a number';
if (!isNaN(number)) {
  message = `My number: ${number}`;
}
console.log(message);
