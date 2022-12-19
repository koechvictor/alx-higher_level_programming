#!/usr/bin/node

const first = 'undefined';

console.log((process.argv[2] || first) + ' is ' + (process.argv[3] || first));
