#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) =>
  (error) ? console.error(error) : console.log(computeTasks(JSON.parse(body))));

function computeTasks (jsonTasks) {
  const completed = {};
  for (const i in jsonTasks) {
    if (jsonTasks[i].completed === true) {
      if (completed[jsonTasks[i].userId] === undefined) {
        completed[jsonTasks[i].userId] = 1;
      } else {
        completed[jsonTasks[i].userId]++;
      }
    }
  }
  return completed;
}
