#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const ans = {};
  for (const info of body) {
    if (info.completed === true) {
      if (isNaN(ans[String(info.userId)])) {
        ans[String(info.userId)] = 1;
      } else {
        ans[String(info.userId)] += 1;
      }
    }
  }
  console.log(ans);
});
