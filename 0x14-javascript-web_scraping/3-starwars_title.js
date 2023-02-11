#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = 'http://swapi.co/api/films/';

function getStatusJson (theUrl) {
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
      const status = res.statusCode;
      console.log(json.title);
      return (status, json);
    }
  });
}

getStatusJson(url + argv[2]);
