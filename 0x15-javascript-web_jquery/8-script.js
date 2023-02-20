$.get('https://swapi.co/api/films/?format=json', function (x) {
  for (const film of x.results) {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  }
});
