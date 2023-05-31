#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request.get(url, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body).characters;
  const promises = [];

  data.forEach((o, i) => {
    promises.push(new Promise((resolve, reject) => {
      return request.get(o, function (error, res, body1) {
        if (error) {
          reject(new Error('Something went wrong'));
        }
        resolve(JSON.parse(body1).name);
      });
    }));
  });

  Promise.all(promises).then(data => {
    data.forEach((o) => {
      console.log(o);
    });
  });
});
