document.getElementById('prediction-form').addEventListener('submit', function(e) {
    e.preventDefault();

    // Collect form data
    let temperature = document.getElementById('temperature').value;
    let humidity = document.getElementById('humidity').value;
    let light = document.getElementById('light').value;
    let co2 = document.getElementById('co2').value;
    let humidity_ratio = document.getElementById('humidity_ratio').value;

    // Create a data object
    let data = {
        'temperature': temperature,
        'humidity': humidity,
        'light': light,
        'co2': co2,
        'humidity_ratio': humidity_ratio
    };

    // Send the data to the back-end using Fetch API
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        // Show the result in the result div
        document.getElementById('result').innerHTML = 'Predicted Occupancy: ' + result.occupancy;
    })
    .catch(error => console.error('Error:', error));
});

