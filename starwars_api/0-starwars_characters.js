#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + filmId;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  printCharacters(JSON.parse(body).characters, 0);
});

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], function (err, response, body) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(JSON.parse(body).name);
    printCharacters(characters, index + 1);
  });
}