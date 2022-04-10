#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) =>
  (error) ? console.error(error) : console.log(computeTasks(JSON.parse(body))));

function computeTasks (jsonTasks) {
  const completedTask = jsonTasks.filter((entries) => entries.completed === true);
  const dict = {};

  for (const i in completedTask) {
    if (!dict[completedTask[i].userId]) {
      dict[completedTask[i].userId] = 1;
    } else {
      dict[completedTask[i].userId]++;
    }
  }
  return dict;
}
