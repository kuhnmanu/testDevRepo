# This es a test python file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = 10

# %%: one way to define python code cell
print('one way to define a cell')

x = 10

# %%: another way to define code cell
print('a second one')
x = 2*x
x


# %%: a next cell
# Data for plotting

# Simple tests
print('Hello world!')
17+25

# Print dataframe
pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

# Show plot
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
