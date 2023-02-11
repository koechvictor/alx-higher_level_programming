#!/usr/bin/node

const request = require('request');
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
      const json = JSON.parse(body);
      // const status = res.statusCode;
      // console.log(json);
      const data = json;
      let count = 0;
      const results = data.results;

      for (const i in results) {
        const characters = results[i].characters;
        for (const j in characters) {
          if (characters[j].indexOf('/18/') >= 0) {
            count += 1;
          }
        }
      }
      console.log(count);
      return json;
    }
  });
}

getJson(argv[2]);
