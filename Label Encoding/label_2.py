#importing dependencies
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#loading pandas into the DataFrame

iris_data = pd.read_csv(r'C:/Users/legion/Desktop/Data_Science/Datasets/iris.csv')
# print(iris_data.head())

#Finding counts of different labels.
# print(iris_data['Species'].value_counts())

#Label Encoding:
label_encode = LabelEncoder()
labels = label_encode.fit_transform(iris_data.Species)

#appending the labels to target variable
iris_data['target'] = labels

print(iris_data.head())
print(iris_data['target'].value_counts())
