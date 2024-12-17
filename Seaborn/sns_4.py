import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#load the house price dataset
from sklearn.datasets import load_boston
house_boston=load_boston()

house = pd.DataFrame(house_boston.data, columns=house_boston.feature_names)
house['PRICE'] = house_boston.target