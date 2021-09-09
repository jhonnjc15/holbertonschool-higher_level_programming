#!/usr/bin/node
exports.esrever = function (list) {
  const reverseList = [];
  for (const i of list) {
    reverseList.unshift(i);
  }
  return reverseList;
};
