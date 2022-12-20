#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  const size = list.length - 1;

  for (const i in list) {
    rev[i] = list[size - i];
  }
  return rev;
};
