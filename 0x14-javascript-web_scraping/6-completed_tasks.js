#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const allData = JSON.parse(body);
    const newDict = {};
    for (let i = 0; i < allData.length; i++) {
      if (allData[i].completed === true) {
        if (newDict[allData[i].userId] === undefined) {
          newDict[allData[i].userId] = 1;
        } else {
          newDict[allData[i].userId] += 1;
        }
      }
    }
    console.log(newDict);
  }
});
