#!/usr/bin/node

exports.converter = function (base) {
  return function (ans) {
    return (num.toString(base));
  };
};
