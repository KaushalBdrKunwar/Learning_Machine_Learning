import pandas as pd


#Importing the data from csv file dataset.
diabetes_df = pd.read_csv(r'C:/Users/legion/Desktop/Data_Science/Datasets/diabetes.csv')
# print(df)
print(type(diabetes_df))
print(diabetes_df.shape)

#For First five rows.
print(diabetes_df.head())