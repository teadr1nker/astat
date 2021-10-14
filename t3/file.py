#!/usr/bin/python3
#import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import os, sys
sys.path.append('../common/')
from tex import tex

def density(data, n):
    c, b = np.histogram(data, bins=n)
    return (b[:-1], c)

#1
N = 100
a = 0.0
b = 1.0

data1 = np.random.uniform(a, b, N)
#print(data1)
plt.hist(data1, 20)
plt.xlabel('sample')
plt.ylabel('freq')
plt.savefig('uniform1.png')
plt.clf()

#2
N = 100
a = 2.0
b = 7.0

data2 = np.random.uniform(a, b, N)
#print(data1)
plt.hist(data2, 20)
plt.xlabel('sample')
plt.ylabel('freq')
plt.savefig('uniform2.png')
plt.clf()

#3
N = 100
mean = 6
var = 200
data3 = np.random.normal(mean, var, N)
#norm = stats.norm.rvs(mean, var, N)
#dens = density(norm, 20)
plt.hist(data3, 20)
#plt.plot(dens[0], dens[1])
plt.xlabel('sample')
plt.ylabel('freq')
plt.savefig('norm.png')
plt.clf()

#4
