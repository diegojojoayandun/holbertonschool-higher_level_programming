#!/usr/bin/node

const fs = require('fs');

const fileA = fs.readFileSync(process.argv[2], 'utf8');
const fileB = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFile(process.argv[4], fileA.concat(fileB), 'utf8', (err, data) => (err) ? console.log(err) : null);
