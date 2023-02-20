$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (x) {
  $('DIV#hello').text(x.hello);
});
