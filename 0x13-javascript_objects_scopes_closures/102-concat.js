#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;

const source1 = fs.readFileSync(argv[2], 'utf8');
const source2 = fs.readFileSync(argv[3], 'utf8');

const dest = source1 + source2;
fs.writeFile(argv[4], dest, function (err) {
  if (err) {
    return console.log(err);
  }
});
