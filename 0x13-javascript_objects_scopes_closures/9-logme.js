#!/usr/bin/node

let argc = 0;
exports.logMe = (item) => console.log((argc++) + ': ' + item);
