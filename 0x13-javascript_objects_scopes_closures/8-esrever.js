#!/usr/bin/node
exports.esrever = function (list) {
  const ret = [];
  for (let i = 0; list.length !== 0; i++) {
    ret[i] = list.pop();
  }
  return ret;
};
