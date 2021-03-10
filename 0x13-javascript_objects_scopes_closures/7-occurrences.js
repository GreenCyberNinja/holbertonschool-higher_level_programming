#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  for (const ind of list) {
    if (ind === searchElement) {
      num++;
    }
  }
  return (num);
};
