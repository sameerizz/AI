# Program 8 : Write a program to implement K-Nearest Neighbors (KNN) Algorithm
# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Set the plot style
plt.style.use('ggplot')

# Load the dataset
df = pd.read_csv("diabetes.csv")

# Display the first few rows of the dataset
print(df.head())

# Display the last few rows of the dataset
print(df.tail())

# Display the shape of the dataset
print(df.shape)

# Display the data types of each column
print(df.dtypes)

# Separate features (X) and target variable (y)
X = df.drop('Outcome', axis=1).values
y = df['Outcome'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Define the range of neighbors to consider
neighbors = np.arange(1, 9)

# Initialize arrays to store accuracy scores
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Train and evaluate KNN for different numbers of neighbors
for i, k in enumerate(neighbors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    train_accuracy[i] = knn.score(X_train, y_train)
    test_accuracy[i] = knn.score(X_test, y_test)

# Plot the results
plt.figure(figsize=(10, 6))  # Increase figure size for better visibility
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label='Testing Accuracy')
plt.plot(neighbors, train_accuracy, label='Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.tight_layout()  # Adjust layout to prevent cutting off labels
plt.show()