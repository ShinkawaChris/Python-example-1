#numpy works

import numpy as np
from Cython.Shadow import inline
x = np.array([1,2,3,4])
print(x)
print(x.shape)

#plot works
import matplotlib.pyplot as plt

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
#plt.show()

# import csv works
'''
import csv

data = []
with open('exerciseV1.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      data.append(row)
print(data[:1])
'''

# import with pandas

import pandas as pd

data = pd.read_csv('exerciseV1.csv')

print(data.head())
