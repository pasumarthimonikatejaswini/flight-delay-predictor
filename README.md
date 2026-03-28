# ✈️ Flight Delay Prediction System

## 📌 About the Project

Flight delays are something we all have experienced at some point. They can happen due to many reasons like bad weather, long travel distances, or delays before takeoff. These delays affect passengers as well as airline operations.
In this project, I have built a simple machine learning model that predicts whether a flight will be delayed or not based on a few important factors.
The main idea of this project is to understand how machine learning can be used to solve real-world problems in the aviation field.

## 🎯 Problem Statement
It is not easy to predict flight delays manually because multiple factors are involved. Without proper analysis of data, it becomes difficult to make accurate predictions.

So, the goal of this project is to:
- Use data to understand flight delay patterns  
- Build a model that can predict delays  
- Show how AI can help in better decision making  

## 💡 Approach
To solve this problem, I followed these steps:
1. Created a dataset with relevant flight details  
2. Used those features to train a machine learning model  
3. Built a simple program to take user input and predict delay  

The model classifies flights into:
- On-Time  
- Delayed  

## ⚙️ Features
- Predicts whether a flight will be delayed or not  
- Uses simple and understandable input values  
- Runs directly in Python (no complex setup needed)  
- Easy to use and beginner-friendly  

## 📊 Dataset Details
The dataset used in this project is manually created and contains the following columns:
- Airline → Represented using numbers  
- Distance → Distance of the flight in kilometers  
- Weather → 0 for clear weather, 1 for bad weather  
- Departure Delay → Delay before takeoff in minutes  
- Delayed → Final output (0 = No, 1 = Yes)  

### Example Data:
Airline,Distance,Weather,Departure_Delay,Delayed
1,1500,1,20,1
2,800,0,0,0
3,1800,1,25,1

## 🤖 Model Used
I used **Logistic Regression** for this project.

### Why I chose this model:
- It works well for classification problems  
- Easy to understand and implement  
- Suitable for small datasets  

### Inputs:
- Airline  
- Distance  
- Weather  
- Departure Delay  

### Output:
- 0 → Flight is on time  
- 1 → Flight is delayed  

## 🛠️ Tools and Technologies
- Python  
- Pandas  
- Scikit-learn  
- Pickle  

## 📂 Project Structure

flight-delay-predictor/
│
├── dataset.csv
├── train_model.py
├── predict.py
├── model.pkl
├── README.md
└── requirements.txt

## 🚀 How to Run the Project

### Step 1: Install required libraries
pip install pandas scikit-learn

### Step 2: Train the model
python train_model.py
This will create a trained model file.

### Step 3: Run prediction
python predict.py

## ▶️ How It Works
- The user enters flight details  
- The model processes the input  
- It predicts whether the flight will be delayed  

## 📈 Results
The model is able to predict delays based on given inputs. Since the dataset is small and manually created, the results are basic but still show how machine learning works in real scenarios.

## ⚠️ Limitations
- Dataset is not from real-world sources  
- Limited number of features  

