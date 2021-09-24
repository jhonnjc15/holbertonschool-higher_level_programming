$(document).ready(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: (data) => {
      let filmResults = data.results;
      for (films of filmResults) {
        $('UL#list_movies').append('<li>' + films.title + '</li>');
	    console.log('success', films.title);
	  }
    }
  });
});
