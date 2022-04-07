#!/usr/bin/node

const list = require('./100-data').list;

const newArray = list.map((x, i) => x * i);
console.log(list);
console.log(newArray);
