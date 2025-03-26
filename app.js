document.getElementById('prediction-form').addEventListener('submit', function (e) {
  e.preventDefault();

  const formData = {
      temperature: document.getElementById('temperature').value,
      humidity: document.getElementById('humidity').value,
      light: document.getElementById('light').value,
      co2: document.getElementById('co2').value,
      humidity_ratio: document.getElementById('humidity_ratio').value
  };

  fetch('/predict', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData)
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById('result').innerText = `Predicted Occupancy: ${data.prediction}`;
  })
  .catch(error => console.error('Error:', error));
});
