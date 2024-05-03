fetch("https://swapi-api.alx-tools.com/api/films/?format=json")
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        const results = data.results;
        const $listMovies = $("#list_movies");
        
        results.forEach((movie) => {
            $listMovies.append(`<li>${movie.title}</li>`);
        });
    })
    .catch((error) => {
        console.error('Error fetching data:', error);
    });
