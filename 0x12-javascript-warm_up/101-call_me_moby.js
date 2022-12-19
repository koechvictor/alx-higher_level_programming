#!/usr/bin/node

module.exports = {
  callMeMoby: function (num, func) {
    for (let i = 0; i < num; i++) {
      func();
    }
  }
};
