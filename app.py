from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained model
model = joblib.load('model.pkl')

# Route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = request.get_json()
    temperature = float(data['temperature'])
    humidity = float(data['humidity'])
    light = float(data['light'])
    co2 = float(data['co2'])
    humidity_ratio = float(data['humidity_ratio'])

    # Format the input for the model
    input_data = np.array([[temperature, humidity, light, co2, humidity_ratio]])

    # Predict using the model
    prediction = model.predict(input_data)

    # Return the result as a JSON response
    return jsonify({'occupancy': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)


