#!/usr/bin/node
const request = require('request');
const characterId = 18;
let sum = 0;
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes(characterId.toString())) {
          sum++;
        }
      }
    }
  }
  console.log(sum);
});
