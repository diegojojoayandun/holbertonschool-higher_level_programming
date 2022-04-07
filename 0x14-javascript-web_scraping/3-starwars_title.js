#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
const titleId = process.argv[2];

request(url.concat(titleId), (error, response, body) => (error) ? console.error(error) : console.log(JSON.parse(body).title));
