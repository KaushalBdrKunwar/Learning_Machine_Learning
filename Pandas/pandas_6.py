import pandas as pd


#Importing the data from csv file dataset.
diabetes_df = pd.read_csv(r'C:/Users/legion/Desktop/Data_Science/Datasets/diabetes.csv')

#Correlation in pandas
print(diabetes_df.corr())