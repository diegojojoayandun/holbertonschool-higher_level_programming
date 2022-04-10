#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) =>
  (error) ? console.error(error) : console.log(computeTasks(JSON.parse(body))));

function computeTasks (jsonTasks) {
  const completeTask = jsonTasks.filter((entries) => entries.completed === true);
  const dict = {};

  for (const i in completeTask) {
    if (!dict[completeTask[i].userId]) {
      dict[completeTask[i].userId] = 1;
    } else {
      dict[completeTask[i].userId]++;
    }
  }
  return dict;
}
