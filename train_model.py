import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

# Features and target
X = data[["Airline", "Distance", "Weather", "Departure_Delay"]]
y = data["Delayed"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save model
pickle.dump(model, open("model.pkl", "wb"))

from sklearn.metrics import confusion_matrix

# Predict on test data
y_pred = model.predict(X_test)

# Create confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Print confusion matrix in readable format
print("\nConfusion Matrix (Rows=Actual, Columns=Predicted):")
print("             Predicted On-Time  Predicted Delayed")
print(f"Actual On-Time        {cm[0][0]}                 {cm[0][1]}")
print(f"Actual Delayed        {cm[1][0]}                 {cm[1][1]}")