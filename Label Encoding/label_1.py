# converting the labels into numeric form

#importing dependencies
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#Label Encoding of Breast Cancer Dataset.

#loading the data from csv file to pandas dataframe.

cancer_data = pd.read_csv(r'C:/Users/legion/Desktop/Data_Science/Datasets/breast_cancer_data.csv')
print(cancer_data.head())

#Finding the count of different labels 
print(cancer_data['diagnosis'].value_counts())

#load the Label Encoder Function
label_encode = LabelEncoder()

labels = label_encode.fit_transform(cancer_data.diagnosis)

#appending the labels to the DataFrame
cancer_data['target'] = labels

#0--->Benign
#1--->Malignant

print(cancer_data.head())

print(cancer_data['target'].value_counts())