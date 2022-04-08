#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log('error', error);
  } else { console.log('Code:', response && response.statusCode); }
});
