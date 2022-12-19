#!/usr/bin/node

const first = 'No argument';
const second = 'Argument found';
const third = 'Arguments found';

const numOfArgs = process.argv.length;

if (numOfArgs < 3) {
  console.log(first);
} else if (numOfArgs < 4) {
  console.log(second);
} else {
  console.log(third);
}
