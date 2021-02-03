#!/usr/bin/node

const list = process.argv;
list.splice(0, 2);
if (list.length < 2) {
  console.log(0);
} else {
  list.sort((a, b) => a - b);
  console.log(list[list.length - 2]);
}
