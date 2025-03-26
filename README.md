# Occupancy Detection Web Application
Overview
This project is a web-based machine learning application that predicts whether a room is occupied based on sensor data like temperature, humidity, light, CO2, and humidity ratio. The prediction is made using a trained Random Forest model.

The application allows users to input real-time sensor data via a web interface, and the backend (built with Flask) returns a prediction about whether the room is occupied (1) or not (0).

Features
Predict room occupancy based on environmental data.

Interactive front-end for user input of sensor data.

Uses a pre-trained Random Forest classifier for predictions.

Simple and intuitive web interface using HTML, CSS, and JavaScript.

#Tech Stack
Front-end: HTML, CSS, JavaScript

Back-end: Flask (Python)

Machine Learning: Random Forest Classifier (using Scikit-learn)

Model Saving/Loading: Joblib

The application will display:

Occupied (1) if the room is predicted to be occupied.

Not Occupied (0) if the room is predicted to be unoccupied.
