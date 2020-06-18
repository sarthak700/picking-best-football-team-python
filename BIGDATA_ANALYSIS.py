from typing import Any, Union

import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as py
from pandas import Series, DataFrame

df=pd.read_csv('C:\score.csv')
#df=df.head(10)
del df['National_Kit']
print(df.head(10))
#sb.countplot(y=df.Nationality)
#sb.countplot(y='Age',data=df)
#or x="Age",data=df inside count plot
#FINDING GOAL KEEPER
a=0.5
b=1
c=2
d=3
#WEIGHTS
df["gk_Shot_Stopper"]=(d*df.GK_Handling+a*df.GK_Diving+c*df.GK_Reflexes)#new columns being added
df["gk_Sweeper"]=(a*df.GK_Handling+a*df.GK_Diving+d*df.GK_Reflexes+d*df.GK_Kicking)
sd1=df.sort_values("gk_Shot_Stopper",ascending=False)
x1=np.array(list(sd1['Name']))
y1=np.array(list(sd1['gk_Shot_Stopper']))
#sb.barplot(x1,y1,palette='colorblind')
py.ylabel('SHOT STOPPING SCORE')

sd1=df.sort_values("gk_Sweeper",ascending=False)
sd1=sd1.head(5)#top 5 picked from list of 17,000 here is  first big data analysis
x1=np.array(list(sd1['Name']))
y1=np.array(list(sd1['gk_Sweeper']))

#sb.barplot(y1,x1,palette='colorblind')
#py.ylabel('GK SWEEPER SCORE')


#best defenders 2 center backs 2 wing  backs


df['center_backs']=(a*df.Reactions+b*df.Speed+c*df.Interceptions+d*df.Sliding_Tackle)/100
df['wing_backs']=(d*df.Reactions+a*df.Aggression+c*df.Interceptions+a*df.Marking+a*df.Speed+d*df.Sliding_Tackle)/100
sd1=df.sort_values("wing_backs",ascending=False)
sd1=sd1.head(3)
x1=np.array(list(sd1['Name']))
y1=np.array(list(sd1['wing_backs']))
py.xlabel('WING DEFENDERS')
py.ylabel('SCORE')
py.legend()
sb.barplot(x1,y1,palette='colorblind')













py.show()









