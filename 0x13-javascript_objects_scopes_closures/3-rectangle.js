#!/usr/bin/node

module.exports = class Rectangle {
  constructor (width, height) {
    if (width >= 1 && height >= 1) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
