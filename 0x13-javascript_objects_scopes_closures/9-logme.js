#!/usr/bin/node

let argc = 0;
exports.logMe = (element) => console.log((argc++) + ': ' + element);
