import pandas as pd
import numpy as np


#Importing the data from csv file dataset.
diabetes_df = pd.read_csv(r'C:/Users/legion/Desktop/Data_Science/Datasets/diabetes.csv')


#Statistical Measures

#1. Count or number of values.
print(diabetes_df.count())

#2. Mean value - column wise
print(diabetes_df.mean())

#3. Standard deviation - column wise
print(diabetes_df.std())

#4. Minimum value
print(diabetes_df.min())

#5. Maximum value
print(diabetes_df.max())

#all the statistical measures about the dataframe
print(diabetes_df.describe())