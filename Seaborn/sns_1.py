import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Seaborn has some built-in datasets

#1. total bill vs tip dataset
tips = sns.load_dataset('tips')
print(tips.head())

#setting a theme for the plot
sns.set_theme()

#Visualtize the data.
sns.relplot(data=tips, x ='total_bill',y='tip',col='time',hue='smoker',style='smoker',size='size')
print(plt.show())