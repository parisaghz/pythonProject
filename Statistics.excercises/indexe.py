import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from scipy.stats import spearmanr

df = pd.read_csv('/Users/parisa/Downloads/indexes.csv')
df.head(20)
# df = df.dropna(0)
print(df)
x_values = df["SP500"]
y_values = df["NDX"]
plt.scatter(x_values, y_values)
plt.show()

corr, _ = pearsonr(x_values, y_values)
print("Pearson's correlation coefficient = ", corr)
corr, _ = spearmanr(x_values, y_values)
print("Spearman's correlation coefficient = ", corr)
#TODO