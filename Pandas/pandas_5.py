import pandas as pd
import numpy as np


#Importing the data from csv file dataset.
diabetes_df = pd.read_csv(r'C:/Users/legion/Desktop/Data_Science/Datasets/diabetes.csv')


#Manipulating a DataFrame.

#1. Adding a column to a dataFrame.
diabetes_df['Price'] = diabetes_df.Glucose
print(diabetes_df.head())

#2. Removing a row
print(diabetes_df.drop(index=0, axis=0))

#3. Drop a column
print(diabetes_df.drop(columns='Price',axis=1))
 
#4.locating a row using index value.
print(diabetes_df.iloc[2])

#5.locating a particular column.
print(diabetes_df.iloc[:,0])# first column