# -*- coding: utf-8 -*-
"""Zomato Data Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K7NAbQ7557EHuwl6VOrnlewqPHxfl41X
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv("/content/Zomato-data-.csv")
print(dataframe.head())

def handleRate(value):
    value=str(value).split('/') # here the split function used to remove the '/' symbol.
    # moreover which is used to split() is used split the strings into substrings
    value=value[0];
    return float(value)
dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())

dataframe.info() #which is used to provides the details no.of rows,columns Datatypes Moreover null values in a column...

sns.countplot(x=dataframe['listed_in(type)'])#The countplot() in Seaborn is used to visualize the count of categorical data using a bar chart.
plt.xlabel("Type of restaurant")

grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c='green', marker='o')
plt.xlabel('Type of restaurant', c='blue', size=20)
plt.ylabel('Votes', c='red', size=20)

max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']

print('Restaurant(s) with the maximum votes:')
print(restaurant_with_max_votes)

sns.countplot(x=dataframe['online_order'])

sns.countplot(x=dataframe['book_table'])

plt.hist(dataframe['rate'],bins=5)
plt.title('Ratings Distribution')
plt.show()

couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)

plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = dataframe)

plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = dataframe)