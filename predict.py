import pickle
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))

print("✈️ Flight Delay Predictor (Advanced)")

airline = int(input("Enter Airline Code (1-3): "))
distance = float(input("Enter Distance (km): "))
weather = int(input("Weather (0=Clear, 1=Bad): "))
dep_delay = float(input("Departure Delay (minutes): "))

# Create DataFrame with column names
input_data = pd.DataFrame([[airline, distance, weather, dep_delay]],
                          columns=["Airline", "Distance", "Weather", "Departure_Delay"])

# Prediction
prediction = model.predict(input_data)[0]
prob = model.predict_proba(input_data)[0][1]  # Probability of delay

risk = ""
if prob < 0.3:
    risk = "Low"
elif prob < 0.7:
    risk = "Medium"
else:
    risk = "High"

print(f"\n⚠️ Prediction: {'DELAYED' if prediction==1 else 'ON TIME'}")
print(f"Probability of Delay: {prob*100:.2f}%")
print(f"Risk Level: {risk}")