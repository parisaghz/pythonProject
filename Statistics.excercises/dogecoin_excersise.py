import pandas as pd 
import numpy as np 
import os 
import matplotlib.pyplot as plt 

# df2 = pd.read_csv("/Users/parisa/Documents/pythonProject/histogram1.csv")
# print(df2)

# df1 = pd.read_csv("/Users/parisa/Documents/pythonProject/Dogecoin_USD_data.numbers.csv")
# print(df1)


list = [0,1,2,3,4,5,6,7]
for i in range(0,7):
    list[i-1]=list[i]

for i in range(0,6):
    print(list[i], " ")
