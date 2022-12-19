#!/usr/bin/node

const num = process.argv[2];

if (isNaN(parseInt(+num))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(+num); i++) {
    console.log('C is fun');
  }
}
