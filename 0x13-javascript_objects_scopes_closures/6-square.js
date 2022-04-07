#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  privatePrint (caracter) {
    for (let i = 0; i < this.height; i++) {
      let j = 0;
      for (; j < this.width; j++) {
        process.stdout.write(caracter);
      }
      if (j === this.width) {
        console.log('');
      }
    }
  }

  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.height; i++) {
        let j = 0;
        for (; j < this.width; j++) {
          process.stdout.write('X');
        }
        if (j === this.width) {
          console.log('');
        }
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        let j = 0;
        for (; j < this.width; j++) {
          process.stdout.write('C');
        }
        if (j === this.width) {
          console.log('');
        }
      }
    }
  }
}
module.exports = Square;
