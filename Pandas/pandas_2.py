import pandas as pd
import numpy as np


#Importing the data from csv file dataset.
diabetes_df = pd.read_csv(r'C:/Users/legion/Desktop/Data_Science/Datasets/diabetes.csv')


#creating a dataFrame with random values.
random_df = pd.DataFrame(np.random.randint(0,10,(5,5)))
print(random_df)
print(type(random_df))