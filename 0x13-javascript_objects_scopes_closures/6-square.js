#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      let i = 0;
      do {
        i++;
        console.log('X'.repeat(this.width));
      } while (i < this.height);
    } else {
      let i = 0;
      do {
        i++;
        console.log('c'.repeat(this.width));
      } while (i < this.height);
    }
  }
}
module.exports = Square;
