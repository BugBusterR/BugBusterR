# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rkrMc8SCnX19SpoNSYKH68D5dglW0y0a
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/content/tested.csv")
df.head()

df.shape

df.describe()

df['Survived'].value_counts()

#visualization
sns.countplot(x=df['Survived'], hue=df['Pclass'])

df['Sex']

df.shape

df.describe()

#survival wrt gender
sns.countplot(x=df['Sex'], hue=df['Survived'])

#survival rate by sex
df.groupby('Sex')[['Survived']].mean()

df['Sex'].unique()

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
df['Sex']= labelencoder.fit_transform(df['Sex'])
df.head()

df['Sex'], df['Survived']

sns.countplot(x=df['Sex'], hue=df['Survived'])

df.isna().sum()

df=df.drop(['Age'], axis=1)

df_final = df
df_final.head(10)

X= df[['Pclass','Sex']]
Y= df['Survived']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LogisticRegression
log= LogisticRegression(random_state=0)
log.fit(X_train,Y_train)

pred=print(log.predict(X_test))

print(Y_test)

import warnings
warnings.filterwarnings('ignore')
res= log.predict([[2,1]])
if (res==0):
  print ('Sorry not survived')
else:
  print("survived")