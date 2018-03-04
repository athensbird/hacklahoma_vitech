import csv
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("Vitech_Data_06.csv", dtype = {"PURCHASED":object, "MARITAL_STATUS":int,"TOBACCO":int})

# Create arrays for the features and the response variable
y = df['PURCHASED'].values
X = df.drop('PURCHASED', axis = 1).values

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=21, stratify=y)

# Create a k-NN classifier with 9 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=11)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Print the accuracy
print(knn.score(X_test, y_test))