import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#load the titanic dataset
titanic = sns.load_dataset('titanic')
print(titanic.head())

#Count Plot
sns.countplot(x='class',data=titanic)
print(plt.show())

print(titanic.shape)

#Bar_Graph
sns.barplot(x='sex',y='survived',hue='class',data=titanic)
print(plt.show())