document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('recommendation-form');
    const recommendationsDiv = document.getElementById('recommendations');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const musicType = document.getElementById('music_type').value;
        const numSongs = document.getElementById('num_songs').value;

        fetch('/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ music_type: musicType, num_songs: numSongs })
        })
        .then(response => response.json())
        .then(data => {
            recommendationsDiv.innerHTML = '';
            if (data.songs) {
                data.songs.forEach(song => {
                    const songElement = document.createElement('p');
                    songElement.textContent = song;
                    recommendationsDiv.appendChild(songElement);
                });
            } else {
                recommendationsDiv.textContent = 'No recommendations available.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
