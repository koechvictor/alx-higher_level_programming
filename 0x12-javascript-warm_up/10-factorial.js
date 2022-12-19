#!/usr/bin/node

const a = parseInt(+process.argv[2]);

function factorial (a) {
  if (a <= 1) {
    return 1;
  }
  return a * factorial(a - 1);
}

if (isNaN(a)) {
  console.log(1);
} else {
  console.log(factorial(a));
}
