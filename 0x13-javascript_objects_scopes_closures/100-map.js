#!/usr/bin/node
const list = require('./100-data.js').list;
consol.log(list);
consol.log(list.map((value, index) => value * index));
