📌 Overview :

This project implements a Titanic Survival Predictor using Machine Learning.

It uses Logistic Regression to predict whether a passenger survived or not based on features like age, gender, fare, and passenger class.
The project includes data visualization, preprocessing, model training, and evaluation.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

🏗️ Architecture Diagram :

            +----------------------+
            |     Dataset (CSV)    |
            | TitanicDataset.csv   |
            +----------+-----------+
                       |
                       v
            +----------------------+
            |   Data Preprocessing |
            | Cleaning & Encoding  |
            +----------+-----------+
                       |
                       v
            +----------------------+
            |   Feature Selection  |
            +----------+-----------+
                       |
                       v
            +----------------------+
            |   Train/Test Split   |
            +----------+-----------+
                       |
                       v
            +----------------------+
            | Logistic Regression  |
            |   Model Training     |
            +----------+-----------+
                       |
                       v
            +----------------------+
            |   Prediction & Eval  |
            | Accuracy, CM, Report |
            +----------------------+

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚙️ Features :

📊 Data visualization using seaborn & matplotlib
🧹 Data preprocessing and cleaning
🔢 Feature encoding using pandas
🤖 Logistic Regression model
📈 Performance evaluation (accuracy, confusion matrix, report)
📉 Train-test split for validation

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

🚀 How to Run :

▶️ Command :
  python Titanic.py

Make sure dataset file (TitanicDataset.csv) is in same directory.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

🔄 Workflow :

Load dataset using pandas
Visualize dataset using seaborn
Clean and preprocess data
Convert categorical data into numeric form
Split dataset into training and testing
Train Logistic Regression model
Predict test data
Evaluate results

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

📚 Libraries Used :

Library       Purpose
numpy         Numerical operations
pandas        Data manipulation
seaborn       Data visualization
matplotlib    Plotting graphs
sklearn       Machine learning
math          Mathematical functions

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧠 Functions & Their Usage :

TitanicLogistic()
  Loads dataset
  Performs preprocessing
  Trains model
  Evaluates accuracy

main()
  Entry point of program

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

📊 Model Details :

Algorithm : Logistic Regression
Type : Supervised Learning
Task : Classification

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

📊 Evaluation Metrics :

Accuracy Score
Confusion Matrix
Classification Report

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Report

📊 Sample Output :

Classification report of Logistic Regression is :
Precision, Recall, F1-score values

Confusion Matrix :
[[TN FP]
[FN TP]]

Accuracy :
0.78 (example)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚠️ Limitations :

Accuracy depends on dataset quality
No hyperparameter tuning
Basic preprocessing only
No deployment (CLI-based only)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

🔮 Future Enhancements :

📊 Hyperparameter tuning
📈 Use advanced models (Random Forest, XGBoost)
🌐 Deploy as web app
📉 Improve feature engineering
📊 Add more visual analytics

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
