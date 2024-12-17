#Methods to handle missing values:
#1.Imputation
#2.Dropping

#Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#loading the dataset to the pandas DataFrame
dataset = pd.read_csv(r'C:/Users/legion/Desktop/Data_Science/Datasets/Placement_Dataset.csv')
print(dataset.head())

#dataset misssing values numbers
print(dataset.shape)
print(dataset.isnull().sum())

#Central Tendencies:
#1.Mean
#2.Median
#3.Mode

# # Assuming `dataset.salary` contains the salary data
# fig, ax = plt.subplots(figsize=(8, 8))
# sns.histplot(dataset.salary, kde=True, ax=ax)  # Use sns.histplot for flexibility
# ax.set_title('Distribution of Salary')
# plt.show()
 
 #analyse the distribution of data in the salary
sns.displot(dataset.salary, kde=True, height=8, aspect=1)
plt.title('Distribution of Salary')
plt.show()

#In case of skew(distribution more on one side) we dont use mean instead use median or mode to find missing dataset

#Replace the missing values with Median value.
dataset['salary'].fillna(dataset['salary'].median(),inplace=True)
print(dataset.isnull().sum())

# #filling missing value with mean value.
# dataset['salary'].fillna(dataset['salary'].mean(),inplace=True)
# print(dataset.isnull().sum())
#But we dont mean in this case

#This is all about imputation.

#------------Method_2-----dropping--
salary_dataset = pd.read_csv(r'C:/Users/legion/Desktop/Data_Science/Datasets/Placement_Dataset.csv')
print(salary_dataset.shape)
print(salary_dataset.isnull().sum())

#drop missing values.
salary_dataset = salary_dataset.dropna(how='any')
print(salary_dataset.isnull().sum())