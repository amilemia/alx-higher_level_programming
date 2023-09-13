#!/usr/bin/node
const ParentSquare = require('./5-square.js');

class Square extends ParentSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let square = '';
      for (let j = 0; j < this.width; j++) {
        square += c;
      }
      console.log(square);
    }
  }
}

module.exports = Square;
