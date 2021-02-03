#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('yay');
} else {
  console.log('My number: %d', process.argv[2]);
}
