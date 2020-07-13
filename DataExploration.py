import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


file = "C:/Users/Benra/OneDrive/Documents/VideoGameSales/vgsales.csv"

df = pd.read_csv(file)

df
gs = df[['Genre', 'Global_Sales']].groupby('Genre').agg('sum')
gs.reset_index(level=0, inplace=True)

g = gs['Genre']
s = gs['Global_Sales']

fig = px.bar(x=g, y=s, color=g, labels={'Genre':'Global Sales (in millions)'})
fig.show()
