#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const argv = process.argv;
// const url = 'http://swapi.co/api/films/';

function getJson (theUrl) {
  const options = {
    url: theUrl,
    method: 'GET',
    headers: {
      Accept: 'application/json',
      'Accept-Charset': 'utf-8'
    }
  };
  request(options, function (err, res, body) {
    if (err) {
      console.log(err);
    } else {
      fs.writeFile(argv[3], body, (err) => {
        if (err) {
          return console.log(err);
        }
      });
      // const json = JSON.parse(body);
      // const status = res.statusCode;
      // console.log(json);
    }
  });
}

getJson(argv[2]);
