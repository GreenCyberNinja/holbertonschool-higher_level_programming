#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) console.log(err);

  const parsedBody = JSON.parse(body).results;
  const films = parsedBody.filter(film => {
    for (const wedge of film.characters) {
      if (wedge.includes('18')) return (true);
    }
    return (false);
  });
  console.log(films.length);
});
