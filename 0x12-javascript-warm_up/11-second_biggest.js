#!/usr/bin/node

const a = process.argv;
const size = a.length;

function secondBiggest (a) {
  a.sort((a, b) => b - a);
  return a[1];
}

if (size < 4) {
  console.log(0);
} else {
  console.log(secondBiggest(a.slice(2, size)));
}
