#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  for (let ind = 0; ind < process.argv[2]; ind++) {
    console.log('C is fun');
  }
}
