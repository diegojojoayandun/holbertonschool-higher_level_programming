#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, body) =>
  (error) ? console.error(error) : allCharacters(JSON.parse(body).characters));

function allCharacters (oChracters) {
  oChracters.forEach((url) => request(url, (error, response, body) =>
    (error) ? console.error(error) : console.log(JSON.parse(body).name)));
}
