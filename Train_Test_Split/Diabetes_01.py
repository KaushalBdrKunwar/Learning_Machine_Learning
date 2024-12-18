import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

#Data Collection and Analysis:

#loading diabetes dataset
diabetes_dataset = pd.read_csv(r'C:/Users/legion/Desktop/Data_Science/Datasets/diabetes.csv')
# print(diabetes_dataset.head())

#no. of rows and columns in this dataset.
# print(diabetes_dataset.shape)

#getting the statistical measures of the data.
# print(diabetes_dataset.describe())

print(diabetes_dataset['Outcome'].value_counts())
#0--> Non Diabetec
#1--> Diabetec

# print(diabetes_dataset.groupby('Outcome').mean())

#Seperating data into data and labels.
X = diabetes_dataset.drop(columns='Outcome', axis=1) #Feature
Y = diabetes_dataset['Outcome'] #Target

#--------------DataStandardization------------------#
scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)
# print(standardized_data)

X= standardized_data
Y= diabetes_dataset['Outcome']

# print(X)
# print(Y)

#------------------Spliting the Data into training and testing Data-------#
X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.2, random_state=2)

print(X.shape,X_train.shape,X_test.shape)