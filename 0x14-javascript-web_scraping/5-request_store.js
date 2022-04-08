#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], (error, response, body) => (error)
  ? console.error(error)
  : fs.writeFile(process.argv[3],
    body && response.body, 'utf8', (err, data) => (err) ? console.log(err) : null));
