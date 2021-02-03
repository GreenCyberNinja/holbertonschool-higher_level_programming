#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Missing sizes');
} else {
  for (let ind = 0; ind < process.argv[2]; ind++) {
    let row = '';
    for (let j = 0; j < process.argv[2]; j++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
