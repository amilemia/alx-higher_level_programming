#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let n = 0;

  for (const i in list) {
    if (list[i] === searchElement) {
      n++;
    }
  }
  return (n);
};
