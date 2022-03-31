#!/usr/bin/node

exports.addMeMaybe = (x, theFunction) => {
  ++x;
  theFunction(x);
};
