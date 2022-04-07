#!/usr/bin/node

const myList = require('./100-data').list;

console.log(myList);
let count = -1;
console.log(myList.map(function (x) {
  count++;
  return (x * count);
}));