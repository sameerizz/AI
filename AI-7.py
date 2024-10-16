# Program 7: Write a program to implement Naive Bayes Algorithm
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
import seaborn as sns
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv("disease.csv")

# Display the first few rows of the dataset
print(df.head())

# Display the last few rows of the dataset
print(df.tail())

# Display information about the dataset
df.info()

# Initialize LabelEncoder
le = LabelEncoder()

# Encode categorical variables
df['Sore Throat'] = le.fit_transform(df['Sore Throat'])
df['Fever'] = le.fit_transform(df['Fever'])
df['Swollen Glands'] = le.fit_transform(df['Swollen Glands'])
df['Congestion'] = le.fit_transform(df['Congestion'])
df['Headache'] = le.fit_transform(df['Headache'])
df['Diagnosis'] = le.fit_transform(df['Diagnosis'])
print(df)

# Visualize the distribution of 'Sore Throat'
fig, ax = plt.subplots(figsize=(6,6))
sns.countplot(x='Sore Throat', data=df)
plt.title("Category-wise count of Sore Throat")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# Visualize the distribution of 'Fever'
fig, ax = plt.subplots(figsize=(6,6))
sns.countplot(x='Fever', data=df)
plt.title("Category-wise count of Fever")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# Visualize the distribution of 'Congestion'
fig, ax = plt.subplots(figsize=(6,6))
sns.countplot(x='Congestion', data=df)
plt.title("Category-wise count of Congestion")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# Visualize the distribution of 'Headache'
fig, ax = plt.subplots(figsize=(6,6))
sns.countplot(x='Headache', data=df)
plt.title("Category-wise count of Headache")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# Visualize the distribution of 'Diagnosis'
fig, ax = plt.subplots(figsize=(6,6))
sns.countplot(x='Diagnosis', data=df)
plt.title("Category-wise count of Diagnosis")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# Prepare features and target variable
X = df.drop('Diagnosis', axis=1)
y = df['Diagnosis']

# Initialize and train the Multinomial Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X,y)

# Make predictions
y_pred = classifier.predict(X)

# Print evaluation metrics
print("Confusion matrix")
print("confusion matrix:\n",confusion_matrix(y, y_pred))

print("Classification report:\n",classification_report(y, y_pred))

print("Accuracy score:\n",accuracy_score(y, y_pred))

print("Precision score:\n",precision_score(y, y_pred, average='weighted'))

print("Recall score:\n",recall_score(y, y_pred, average='weighted'))

print("F1 score:\n",f1_score(y, y_pred, average='weighted'))