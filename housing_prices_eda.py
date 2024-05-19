# -*- coding: utf-8 -*-
"""housing_prices eda.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j6G_hDUsod3JBRo6LsI8fbAr_wkP1_L2
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
sns.set(color_codes=True)
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

df=pd.read_csv("/content/housing_prices.csv",encoding="latin-1",na_values="?")
df

#Summary Statistics
df.describe()

df[df.duplicated()]

df.info()

print(df.isnull().sum())



#converting column names to lowercase
df.columns=df.columns.str.lower()
df.columns

df.head()

#Summary Statistics after handling missing values
df.describe()

df.drop(columns=["mainroad","guestroom","hotwaterheating"],axis=1,inplace=True)
df.head()

#Ploting outliers using boxplots
sns.boxplot(x=df["area"])
plt.show()

#Ploting outliers using boxplots
sns.boxplot(x=df["price"])
plt.show()

df1=df.loc[:,df.dtypes!=object]
df1

l=list(df.loc[:,df.dtypes!=object].columns)
l

#Removing Outiers using z-scores
z=np.abs(stats.zscore(df[l]))
z

#tranforming data after modifying/removing outliers
threshold=3
df3=df[(z<threshold).all(axis=1)]
df3

#Checking Intial and Final data
print(df.shape)
print(df3.shape)

df3.info()

df3.to_csv("/content/sales.1.csv")

#coorelations between columns
corr=df1.corr()
corr

#ploting cooreation matrix
plt.figure(figsize=(12,8))
sns.heatmap(corr,cmap='BrBG',annot=True)
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['area'], bins=10, kde=True)
plt.title('housing graph')
plt.xlabel('price')
plt.ylabel('area')
plt.show()

sns.distplot(df['bedrooms'])
plt.show()