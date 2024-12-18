#Importing the dependencies
import numpy as np
import pandas as pd

#loading the dataset to pandas DataFrame
diabetes_df = pd.read_csv(r'C:/Users/legion/Desktop/Data_Science/Datasets/diabetes.csv')

#First five rows of dataframe
print(diabetes_df.head())

#Check the null value
# print(diabetes_df.isnull().sum())
#no null values

# distribution of the two classes
# print(diabetes_df['Outcome'].value_counts())
#---> Imaballanced but not highly imbalanced 

#Handeling imbalanced datasets

#seperating the non diabetic and diabetic 
diabetic = diabetes_df[diabetes_df.Outcome == 1]
non_diabetic = diabetes_df[diabetes_df.Outcome == 0]
print(diabetic.shape)
print(non_diabetic.shape)

#Under-sampling
#Build a sample dataset containing similar distribution of diabetic and non-diabetic

#Number of diabetic sample-->268
non_diabetic_sample = non_diabetic.sample(n=268)
print(non_diabetic_sample.shape)

#Concatenate the two DataFrames
new_dataset = pd.concat([non_diabetic_sample,diabetic],axis= 0)
print(new_dataset.head())

print(new_dataset['Outcome'].value_counts())