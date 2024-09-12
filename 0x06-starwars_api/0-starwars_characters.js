#!/usr/bin/node
/**
 * Script that prints all characters of a Star Wars movie in the same order
 * as they appear in the "characters" list in the /films/ endpoint.
 * Usage: ./0-starwars_characters.js <Movie ID>
 */

const request = require('request');

// Get the Movie ID from command line arguments
const movieId = process.argv[2];

// Check if a movie ID is provided
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// URL for the specific Star Wars movie using the Movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to the Star Wars API for the movie data
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const movieData = JSON.parse(body);

  // Get the list of character URLs
  const characters = movieData.characters;

  // Create an array of Promises, one for each character request
  const promises = characters.map((characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }

        // Parse the character data and resolve the Promise with the name
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  });

  // Use Promise.all to wait for all requests to complete
  Promise.all(promises)
    .then((characterNames) => {
      // Print each character name in order
      characterNames.forEach((name) => {
        console.log(name);
      });
    })
    .catch((error) => {
      console.error(error);
    });
});
