# Program 5: Write a program to implement Support Vector Machine (SVM) Algorithm
# Install necessary packages (uncomment and run in your terminal if needed)
# pip3 install pandas scikit-learn

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Set display options for pandas dataframes
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 1000)

# Load the dataset
diabetes = pd.read_csv('diabetes.csv')
diabetes 
# Display the first and last few rows of the dataset
print(diabetes.head())
print(diabetes.tail())


# Split features and target variable
x = diabetes.drop(columns='Outcome')  # Assuming 'Outcome' is the target variable
y = diabetes['Outcome']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)
print('y_train shape:', y_train.shape)
print('y_test shape:', y_test.shape)

# Initialize and fit the SVC model
support_vector_classifier = SVC(kernel='linear').fit(x_train, y_train)

# Make predictions
y_pred = support_vector_classifier.predict(x_test)

# Confusion matrix and accuracy
cm = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:\n', cm)
print('Accuracy:', accuracy_score(y_test, y_pred))

# Optional: Display the classification report
print('Classification Report:\n', classification_report(y_test, y_pred))