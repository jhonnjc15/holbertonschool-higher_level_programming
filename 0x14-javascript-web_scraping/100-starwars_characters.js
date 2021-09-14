#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const allData = JSON.parse(body).results;
    for (let i = 0; i < allData.length; i++) {
      if (allData[i].url.includes(movieId.toString())) {
        for (const characters of allData[i].characters) {
          request(characters, (error, resp, body_) => {
            if (error) {
              console.log(error);
            } else {
              console.log(JSON.parse(body_).name);
            }
          });
        }
      }
    }
  }
});
