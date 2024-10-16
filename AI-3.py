# Program 3: Write a program to implement Decision Tree Algorithm

# Import necessary libraries
import numpy as np  # For numerical operations
import pandas as pd  # For data manipulation and analysis
import matplotlib.pyplot as plt  # For plotting
from sklearn import tree  # For decision tree classifier
from sklearn.preprocessing import LabelEncoder  # For encoding categorical variables

# Load the dataset from a CSV file
PlayTennis = pd.read_csv("play_tennis.csv")

# Create a LabelEncoder instance for encoding categorical variables
le = LabelEncoder()

# Encode categorical variables using LabelEncoder
# This converts string labels to numeric values
PlayTennis['day'] = le.fit_transform(PlayTennis['day'])
PlayTennis['outlook'] = le.fit_transform(PlayTennis['outlook'])
PlayTennis['temp'] = le.fit_transform(PlayTennis['temp'])
PlayTennis['humidity'] = le.fit_transform(PlayTennis['humidity'])
PlayTennis['wind'] = le.fit_transform(PlayTennis['wind'])
PlayTennis['play'] = le.fit_transform(PlayTennis['play'])

# Define features (X) and target variable (y)
y = PlayTennis['play']  # Target variable is 'play'
X = PlayTennis.drop(['play'], axis=1)  # Features are all columns except 'play'

# Create and fit the Decision Tree classifier
clf = tree.DecisionTreeClassifier(criterion='entropy')  # Using entropy as the splitting criterion
clf.fit(X, y)  # Train the classifier on the data

# Plot the decision tree
plt.figure(figsize=(10, 6))  # Set the figure size
tree.plot_tree(clf, filled=True, feature_names=X.columns, class_names=le.classes_)
# filled=True colors the nodes, feature_names labels the features, class_names labels the classes
plt.show()  # Display the plot