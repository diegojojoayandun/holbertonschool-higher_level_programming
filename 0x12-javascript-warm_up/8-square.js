#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squareSize; i++) {
    let j = 0;
    for (; j < squareSize; j++) {
      process.stdout.write('X');
    }
    if (j === squareSize) {
      console.log('');
    }
  }
}
