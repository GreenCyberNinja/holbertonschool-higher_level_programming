#!/usr/bin/node

exports.esrever = function (list) {
  const ans = [];
  for (const ind of list) {
    ans.unshift(ind);
  }
  return (ans);
};
