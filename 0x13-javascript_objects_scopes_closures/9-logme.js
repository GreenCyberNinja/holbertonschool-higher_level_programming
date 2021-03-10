#!/usr/bin/node

let numin = 0;
exports.logMe = function (item) {
  console.log(numin + ': ' + item);
  numin += 1;
};
