#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

function orderChar (characters, index) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], function (err, response, body) {
    if (err) {
      console.log(err);
    }
    if (response.statusCode === 200) {
      console.log(JSON.parse(body).name);
      return orderChar(characters, index + 1);
    }
  });
}

request(url + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  orderChar(JSON.parse(body).characters, 0);
});
