#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

for (const key in dict) {
  const value = dict[key];
  if (newDict[value]) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
}
console.log(newDict);
