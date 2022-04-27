import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

marvel = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/comic-characters/marvel-wikia-data.csv")

marvel.head()
print(marvel.head(10))


marvel_3 = marvel[['name','ALIGN', 'SEX','Year']]
#help(pd.Series())
#marvel_3.head()
specific_column = ['name','ALIGN', 'SEX','Year']
marvel_4 = marvel[specific_column]
print(marvel_4.head())

dc = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/comic-characters/dc-wikia-data.csv")
marvel_5 = dc.head()
print(dc.head(10))
print(marvel['Year'].min())

fig = plt.scatter(marvel_5['name'], marvel_5['YEAR'])
plt.show()