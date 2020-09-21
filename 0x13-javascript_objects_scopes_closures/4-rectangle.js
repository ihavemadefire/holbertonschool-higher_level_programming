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

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
