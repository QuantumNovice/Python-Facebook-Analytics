#from numpy import *
from matplotlib import pyplot as plt
import random

# This opens up the facebook analytics and loads it into <code>data</code> variable.
with open('nm.csv', 'r') as fd:
    data = fd.readlines()

info = data[:2]
lines = data
data = []
for line in lines:
    words = line.split('\t')
    data.append(words)


def get_category(index):
    '''
    Returns the category you want
    e.g Total Likes, Engagements in US
    '''
    values = []
    for i in data:
        values.append(i[index])
    # category name, category explanation, category values
    return (values[0], values[1], values[2:])

m, d, x = get_category(random.randint(0, len(data[0])))
X=[]
for i in x:
    if i == '':
       X.append(0)
    else: X.append(int(i))
#plt.plot(X)
plt.plot(X)
plt.ylabel(m)
plt.xlabel('days')
plt.show()
