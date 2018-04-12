import pandas as pd
import numpy as np
import datetime

data = pd.DataFrame()


def somefunc():
    pass


# Dealing with mixed type errors in columns
data['c1'].unique()  # gives unique values for determination of diff types

data['c2'].apply(somefunc)  # use apply to apply common function to every value in column

data = data[data['c3'].notnull()]  # removes rows will nan value in specified column

# can combine logical operators to exclude rows by adding & (and), | (or), or ! (not)
data = data[data['c3'].notnull() & data['c4'].isnull() | data['c1'].notnull()]
data.dropna(how='any') # how = any means drop rows that have any nan, how = all is for rows with all nans

data = data[data['c3'] == 'some value']  # get all rows with column as some value
data = data[data['c5'] != 'some value']  # deletes all row with certain entry in c5

# use .groupby function to make agregated data for specific groups
group = data[data['c3'] == 'some value'].groupby('c2')  # creates a groupby object that can then by analyzed
group.count()  # gives counts of each group

"""Remember to use lambda function in apply for quick and dirty functions!"""

# quick lambda function to change string time into a datetime object
data['c1'].apply(lambda x: datetime.datetime.strptime(x, '%m/%d/%Y %I:%M:%S %p'))

"""Functionalize the data cleaning process to make it really easy for you to do W/Out the need to delete or change 
source data"""

