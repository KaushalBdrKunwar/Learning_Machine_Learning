import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#load the iris dataset 
iris = sns.load_dataset('iris')
print(iris.head())

#Scatter Plot
sns.set_theme()
sns.scatterplot(x='sepal_length', y='petal_length',hue='species',data=iris)
print(plt.show())