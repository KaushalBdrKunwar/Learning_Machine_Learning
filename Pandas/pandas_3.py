import pandas as pd


#Importing the data from csv file dataset.
diabetes_df = pd.read_csv(r'C:/Users/legion/Desktop/Data_Science/Datasets/diabetes.csv')

#Inspecting a DataFrame.
#1.Shape
print(diabetes_df.shape)

#2.First Five Rows
print(diabetes_df.head())

#3.Last Five Rows
print(diabetes_df.tail())

#4. Informations about the DataFrame
print(diabetes_df.info())

#5.Find the number of missing values
print(diabetes_df.isnull().sum())

#6. Counting the values based on the labels(here outcomes)
print(diabetes_df.value_counts('Outcome'))

#7. Group the values based on the mean
print(diabetes_df.groupby('Outcome').mean())