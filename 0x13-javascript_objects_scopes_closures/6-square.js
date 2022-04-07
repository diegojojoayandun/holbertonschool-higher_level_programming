#!/usr/bin/node

const squareBase = require('./5-square');

class Square extends squareBase {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let i = 0;
      do {
        i++;
        console.log(c.repeat(this.width));
      } while (i < this.height);
    }
  }
}
module.exports = Square;
