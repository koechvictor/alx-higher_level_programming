$.get('https://swapi.co/api/people/5/?format=json', function (x) {
  $('DIV#character').text(x.name);
});
