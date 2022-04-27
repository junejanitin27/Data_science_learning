import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from io import StringIO

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 24

list_of_dog = StringIO("""name,height,weight
Zero,10,8
Baron,10,10
Nymeria,23,50
Watson,12,30
Lassie,23,55
Madison,11,14
Murphy,18,35
Snoopy,15,25
Mochi,14,20
""")

dogs = pd.read_csv(list_of_dog)

print(dogs)

list_of_cats = StringIO("""name,length,weight
Mirai,12,15
Taki,6,6
Taco,12,12
Milo,13,12
Pixel,8,9
Jasper,13,14
Luca,13,16
Pietro,9,10
Mr. Meowsworth,11,6
""")

cats = pd.read_csv(list_of_cats)
print(cats)

plt.figure(figsize=(12,8))
with plt.xkcd():
    fig_1 = plt.bar('name','weight', data = cats)
    plt.title('Cats Data')
    plt.xlabel("Cats name", fontsize = 14)
    plt.ylabel("Weight", fontsize = 14)
    plt.xticks(rotation = 45)
    #plt.rc('axes', labelsize=BIGGER_SIZE)
    plt.show()

sns.set()

plt.figure(figsize=(12,8))
fig2 = sns.scatterplot('weight','length', data = cats)
fig2.set(title = "Catty", xlabel = "Cat Name", ylabel="Length")
plt.xticks(rotation = 45)
plt.show()

fig3 = px.bar(cats,'name','length')
fig3.show()