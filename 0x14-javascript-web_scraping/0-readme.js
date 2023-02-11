#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;

fs.readFile(argv[2], 'utf8', (err, file) => {
  if (err) {
    console.log(err);
  } else {
    console.log(file);
  }
});
