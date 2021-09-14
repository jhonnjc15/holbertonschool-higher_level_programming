#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + movieId, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const allData = JSON.parse(body).characters;
    for (const charact of allData) {
      request(charact, (err, response, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
