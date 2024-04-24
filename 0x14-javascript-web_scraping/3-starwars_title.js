#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(body.title);
});
