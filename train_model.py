import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load the dataset
file_path = 'datatest.csv'  # Path to your CSV file
data = pd.read_csv(file_path)

# Prepare the data
X = data[['Temperature', 'Humidity', 'Light', 'CO2', 'HumidityRatio']]
y = data['Occupancy']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a RandomForest model (or any other model)
model = RandomForestClassifier()
model.fit(X_train_scaled, y_train)

# Save the trained model to a file using joblib
joblib.dump(model, 'model.pkl')

print("Model saved successfully!")
