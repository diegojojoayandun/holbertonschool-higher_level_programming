#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = '18';

request(url, (error, response, body) =>
  (error) ? console.error(error) : console.log(characterCount(JSON.parse(body).results)));

function characterCount (jsonResults) {
  return jsonResults.filter((entries) =>
    entries.characters.filter((urlMatch) => urlMatch.includes(characterId)).length).length;
}
