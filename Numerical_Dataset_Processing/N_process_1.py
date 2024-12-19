import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#Data_collection and preprocessing.
##loading the data from csv file
diabetes_data = pd.read_csv(r'C:/Users/legion/Desktop/Data_Science/Datasets/diabetes.csv')

#First Five Rows:
# print(diabetes_data.head())

#Number of Rows and Columns
print(diabetes_data.shape)

#Diabetes Discription:
# print(diabetes_data.describe())

#-------Seperating Features and Target---#
X=diabetes_data.drop(columns='Outcome', axis=1)
Y=diabetes_data['Outcome']

# print(X)
# print(Y)
#0---> Not-Diabetes and 1----> Diabetic

#----For Data to be in common Range(Data_standarization)------#
scaler = StandardScaler()
scaler.fit(X)
standarized_X= scaler.transform(X)
print(standarized_X)
#--------Replace X--#
X = standarized_X

#----------Spliting into Train and Test data------#
X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.2, random_state=2)
print(X.shape,X_train.shape,X_test.shape)