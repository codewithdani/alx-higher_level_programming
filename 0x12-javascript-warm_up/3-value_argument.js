#!/usr/bin/node

const [, , firstArgument] = process.argv;

if (firstArgument === undefined) {
    console.log("No argument");
} else {
    console.log(firstArgument);
}
