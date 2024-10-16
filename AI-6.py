# Program 6: Write a program to implement AdaBoost Algorithm
import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_val_score

# LOAD DATASET
gigga = pd.read_csv('diabetes.csv')

# Define the column names
names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']

# Assign the names to the dataframe
dataframe = gigga
dataframe.columns = names

# Convert dataframe to numpy array
array = dataframe.values
X = array[:, 0:8]  # Features
Y = array[:, 8]    # Target variable

seed = 7
num_trees = 30

# Initialize the AdaBoost classifier
model = AdaBoostClassifier(n_estimators=num_trees, random_state=seed, algorithm='SAMME')

# Perform cross-validation
results = cross_val_score(model, X, Y, cv=10)  # Added model and cv parameter

# Print the mean cross-validation score
print('Mean cross-validation score:', results.mean())