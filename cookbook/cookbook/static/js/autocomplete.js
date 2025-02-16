document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search');
    const resultsContainer = document.getElementById('autocomplete-results');

    searchInput.addEventListener('input', function() {
        const query = searchInput.value;
        if (query.length >= 3) {
            fetch(`/acs/?query=${query}`)
                .then(response => response.json())
                .then(data => {
                    resultsContainer.innerHTML = '';
                    data.results.forEach(result => {
                        const li = document.createElement('li');
                        const a = document.createElement('a');
                        a.href = result.url;
                        a.textContent = result.title;
                        li.appendChild(a);
                        resultsContainer.appendChild(li);
                    });
                });
        } else {
            resultsContainer.innerHTML = '';
        }
    });
});

