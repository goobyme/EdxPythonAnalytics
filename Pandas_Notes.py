import pandas as pd
from pandas import Series
from pandas import DataFrame
import numpy as np
import statsmodels.api as sm

# Creating DataFrames with index, rownames a=nd index names
df = DataFrame([['r1', '1', '2', '3', '4'], ['r2', '10', '32', '44', '31']],
               columns=['rowlabels', 'c1', 'c2', 'c3', 'c4'])  # set columns

df.columns = ['a', 'b', 'c']  # rename columns in dataframe
df.set_index('rowlabels', inplace=True)  # set index column , inplace keeps in same df
df.drop(df.index[1,2])  # delete rows in a dataframe (each number is indexed value of column)
del df['c4']  # delete columns in a dataframe

pd.concat([Series, Series], axis=1)  # merge Series together into a DataFrame

# indexing a DF by index or column
c = df['c1']  # access column directly via dictionary method
r1 = df.loc['r1']  # access row data via loc method
r2 = df.iloc[1]  # indexed by integer rather than index name

index_name = df.index[0]  # gets index name
index_values = df.ix[0]  # gets index values for row

col_list = df[['c1', 'c2']]  # list for multiple column selection
row_list_by_value = df[df['c1'] > 20]


cell = df.loc['r1', 'c2']  # get specific cell in loc through regular indexing
chain_cell = df.loc['r1']['c2']  # gets cell value via chain indexing, different in that makes copy of value

slice = df.loc['r1': 'r2']

# Grouping entries together based on column data
df.groupby('c2')  # groups by some categorical data
df.groupby('c1').mean()  # pass method onto grouby to affect values in each group and build DataFrame

# Pandas data from sources
data_list = pd.read_html('url')  # Returns list of all tabular data from given link (no need for own webdl!)

# Sorting rows by column data
df.sort_values('c1', ascending=True)  # for multiple sorts put list in sort and ascending parameters

# Numpy in Pandas and assigning new values in dataframe
df['Cool'] = df[np.where(df['c1'] < df['c2'], 1, 0)]  # assign conditional values onto each row of dataframe
df['c1'].pct_change(2)  # gives percentage change over 2 rows of values in c1 column
df['close'].pct_change().rolling(5).mean()  # constructs Series of rolling 5 day averages for the 1 day pct change

"""REMEMBER TO PLOT SHIT ON IPython USE %matplotlib"""

df.describe()
df.corr()  # gives a correlation matrix of values in each column

# basic Risk Reward can be done by plotting std by mean returns
df.mean()  # Series output of means
df.std()  # Series output of standard div

# Building Regressions

x = df['c1', 'c2']  # Explanatory Variables
y = df['c3']    # Dependent Variable
sm.add_constant(x)

model = sm.OLS(y, x, missing='drop')  # builds model given data set
result = model.fit()  # runs model
result.summary()  # model output

