#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const i of list) {
    if (searchElement === i) {
      counter++;
    }
  }
  return counter;
};
