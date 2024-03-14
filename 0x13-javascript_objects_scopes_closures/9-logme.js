#!/usr/bin/node
exports.logMe = (function (item) {
  let printed = 0;
  return function (item) {
    console.log(printed + ':', item);
    printed += 1;
  };
}());
