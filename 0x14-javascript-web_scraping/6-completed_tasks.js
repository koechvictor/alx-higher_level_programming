#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const newDict = {};
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
      const json = JSON.parse(body);
      // const json = JSON.parse(body);
      // const status = res.statusCode;

      for (const key in json) {
        const value = json[key].userId;

        if (json[key].completed) {
          if (newDict[value]) {
            newDict[value] += 1;
          } else {
            newDict[value] = 1;
          }
        }
      }
      console.log(newDict);
    }
  });
}

getJson(argv[2]);
