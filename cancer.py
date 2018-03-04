from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import pandas as pd

cancer = load_breast_cancer()
raw_data=pd.read_csv('breast-cancer-wisconsin-data-csv', delimiter=',')
raw_data.tail(10)
# print(cancer.feature_names)
# print(cancer.target_names)
