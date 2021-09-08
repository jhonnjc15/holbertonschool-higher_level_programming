#!/usr/bin/node
const args = process.argv;
const nums = [];
let i;
let biggest1;
let biggest2;
if (args.length < 4) {
  console.log(0);
} else {
  for (i = 2; i < args.length; i++) {
    nums.push(parseInt(args[i]));
  }
  biggest1 = Math.max(...nums);
  const index = nums.indexOf(biggest1);
  if (index > -1) {
    nums.splice(index, 1);
  }
  biggest2 = Math.max(...nums);
  console.log(biggest2);
}
