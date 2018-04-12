import numpy as np

x = [[0, 1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15], [20, 21, 22, 23, 24, 25]]

ar = np.array(x, int)

# Index
individual_value_in_array = ar[1, 3]

# Slicing
group_slice_of_array = ar[1:3, 2:4]

# Reshaping array into different x by y in matrix array, error if not equal to total # of entries
ar.reshape(9, 2)

# Initialized matrix array for pre-set range of values
ax = np.arange(10)  # 1D range
ax = np.array(np.arange(4), np.arange(6))  # 2D range of items with each arange object representing a row
ax = np.ones(123)  # range of x number of 1s in range
ax = np.arange(10)**2  # standard math function onto each value
ax = np.identity(10)  # creates identity matrix for given dimension
al = np.linspace(0, 100, 50)  # outputs array of 50 equally spaced values between 0 and 100
arandom = np.random.normal(size=(10,10))  # gens 10x10 box of randomly generated numbers in a normal distribution s = 1

# Can also do basic matrix functions like scalar multiplication or between matrices
az = np.dot(ax, ar)  # Make sure to reshape matrices to be multiplicable
az.transpose()  # also an option to transpose

# Conditional Options
np.where(ax % 2 == 0, True, False)  # Conditional (think IF() in excel)

# Additional stuff
np.array.flat()  # iterator object of an array, can be indexed

# min and argmin() (and max)
ax.max()  # gives the max value within the array
ax.argmin()  # gives the index value that returns the minimal output value
