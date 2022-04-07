#!/usr/bin/node

const fs = require('fs');

const fileA = fs.readFileSync(process.argv[2], 'utf8');
const fileB = fs.readFileSync(process.argv[3], 'utf8');

const fileC = fileA.concat(fileB);

fs.writeFile(process.argv[4], fileC, 'utf8', (err, data) => { if (err) { console.log('no archivo', err); } });
