#!/usr/bin/node

exports.converter = function (base) {
  return function (ans) {
    return (ans.toString(base));
  };
};
