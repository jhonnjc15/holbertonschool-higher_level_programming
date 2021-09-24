$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $('INPUT#language_code').keydown(function (e) {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

translate = () => {
  let url = 'https://www.fourtonfish.com/hellosalut/';
  const languaje = $('INPUT#language_code').val();
  $.get(url + '?lang=' + languaje, (data) => {
    $('DIV#hello').text(data.hello);
  });
}
