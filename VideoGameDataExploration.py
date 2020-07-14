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

fig = px.bar(x=g, y=s, color=g)
# fig.show()


# Let's try to bootstrap the genre/global sales table
# I should revisit the edx course and take a look at the process
# Maybe try to build a knn classifier based on genre?
# Practice regression too, I should try to regress two categories that make sense in corellation

# Guiding Question: Do Japanese sales predict North American sales for video games?

# 1: Create table and standardize units
jna = df[['NA_Sales', 'JP_Sales']]
na_mean = np.mean(jna['NA_Sales'])
na_std = np.std(jna['NA_Sales'])
j_mean = np.mean(jna['JP_Sales'])
j_std = np.std(jna['JP_Sales'])

na_mean
na_std

def standardize(col, mean, std):
    return ((col - mean) / std)

na_sales_standardized = standardize(jna['NA_Sales'], na_mean, na_std)
j_sales_standardized = standardize(jna['JP_Sales'], j_mean, j_std)

jna['NA_Sales_STD'] = na_sales_standardized
jna['JP_Sales_STD'] = j_sales_standardized
jna
fig2 = px.scatter(x=jna['NA_Sales'], y=jna['JP_Sales'])
fig2

# 2: Calculate correlation coefficient, slope and intercept of regression line
def cor(t, x, y):
    return np.mean(t[x]*t[y])

r_val = cor(jna, 'NA_Sales_STD', 'JP_Sales_STD')
r_val

####

def slope(t, x, y, r):
    return r*(np.std(t[y])/np.std(t[x]))

slope_val = slope(jna, 'NA_Sales', 'JP_Sales', r_val)
slope_val

###

def intercept(t, x, y, m):
    return (np.mean(t[y]) - m*np.mean(t[x]))

int_val = intercept(jna, 'NA_Sales', 'JP_Sales', slope_val)
int_val

# This data is terrible for regression- there's no little to no correlation between US and Japanese video game sales somehow
