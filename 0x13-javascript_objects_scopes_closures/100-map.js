#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map((value, index) => value * index);
console.log('Initial List:', list);
console.log('New List:', newList);
