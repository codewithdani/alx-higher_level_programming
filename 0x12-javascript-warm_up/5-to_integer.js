#!/usr/bin/node
const num1 = Math.floor(Number(process.argv[2]));
console.log(isNaN(num1) ? 'Not a number' : `My number: ${num1}`);
