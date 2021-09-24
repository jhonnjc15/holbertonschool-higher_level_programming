$(() => {
  let url = 'https://www.fourtonfish.com/hellosalut/';
  $('INPUT#btn_translate').click( ()=> {
    const languaje = $('INPUT#language_code').val();
	$.get(url + '?lang=' + languaje, (data) => {
        $('DIV#hello').text(data.hello);
    });
  });
});
