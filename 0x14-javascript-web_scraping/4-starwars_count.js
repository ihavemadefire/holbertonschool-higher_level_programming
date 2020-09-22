#!/usr/bin/node
const args = (process.argv);
const request = require('request');
const url = args[2];
const target = 'https://swapi-api.hbtn.io/api/people/18/';
const wedgeList = [];
const retList = [];
request(url, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    results.map(x =>
      wedgeList.push(x.characters));
  }
  wedgeList.map(x => x.includes(target) ? retList.push('stay on target') : {});
  console.log(retList.length);
});
