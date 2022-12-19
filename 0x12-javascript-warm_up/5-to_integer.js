#!/usr/bin/node

const first = 'Not a number';

const arg = process.argv[2];

if (isNaN(parseInt(+arg))) {
  console.log(first);
} else {
  console.log('My number: ' + parseInt(+arg));
}
