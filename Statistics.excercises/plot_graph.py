import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

x_values = np.arange(0.0, 10.0, 0.3)
y_values = np.exp(x_values)

plt.plot(x_values, y_values, linewidth = 3)
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([0.0,10.0,0.0,7000.0])

from scipy.stats import pearsonr
from scipy.stats import spearmanr
corr,_ = pearsonr(x_values, y_values)
print("Pearson's correlation coefficient = ", corr)
corr,_ = spearmanr(x_values, y_values)
print("Searson's correlation coefficient = ", corr)