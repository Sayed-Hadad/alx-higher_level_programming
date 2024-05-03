fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        const results = data;
        $("#hello").text(results.hello)
    })
    .catch((error) => {
        console.error('Error fetching data:', error);
    });
