#!/usr/bin/node
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.get(url, function (data) {
    console.log(data.name);
    $('#character').text(data.name);
  });
});
