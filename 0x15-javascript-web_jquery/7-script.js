$(document).ready(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    success: (people) => {
      $('#character').text(people.name);
      console.log('success')
	}
  })
});
