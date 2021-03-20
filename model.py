import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

df=pd.read_csv('df.csv')
df.head()

df=df.dropna()

from sklearn.preprocessing import LabelEncoder
Le=LabelEncoder()
df['Name']=Le.fit_transform(df['Name'])

df = df.dropna()
df['Day'] = df.index.map(lambda x: x.day)
df['Month'] = df.index.map(lambda x: x.month)
df['Year'] = df.index.map(lambda x: x.year)
x = df[['Name','High','Low','Open','Day','Month','Year']]
y = df['Close']

from sklearn import linear_model
reg = linear_model.LinearRegression()

reg.fit(X,y)

#saving model to disk

pickle.dump(reg, open('model2.pkl','wb'))

#loading model to compare results

model=pickle.load(open('model2.pkl','rb'))

print(model.predict([[0, 731490, 725478, 734975,24, 8, 2021 ]]))
