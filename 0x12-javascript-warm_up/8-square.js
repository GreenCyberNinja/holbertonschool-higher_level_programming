#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
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
