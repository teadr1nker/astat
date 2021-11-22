#!/usr/bin/python3
import numpy as np
from functions import *
import os, sys
sys.path.append('../common/')
import matplotlib.pyplot as plt

tex.printhead()
tex.section('Контрольная работа Миролюбов АК 22404')

V = 18
X = np.loadtxt('First.txt', delimiter=' ')[:,V]
Y = np.loadtxt('Second.txt', delimiter=' ')[:,V]

tex.section('Однородность', 1)
dependency(X, Y)
tex.section('Корреляция', 1)
cor('first', 'second', X, Y)
tex.section('Линейная регрессия', 1)
linreg(X, Y)


tex.printend()

x1=-V
x2=V
x3=V**2+1

p1=1/(V+1)
p2=max([1/((V+1)**2),0.1])
p3 = 1 - p1 - p2
values = [x1, x2, x3]
print(values)
probs = [p1, p2, p3]
data = modelrand(values, probs, 100)
counts, bins = np.histogram(data)
plt.hist(bins[:-1], bins, weights=counts)
plt.show()
plt.clf()
prob = [probs[j] for j in range(len(probs)) if values[j] < 0]
value = [values[j] for j in range(len(values)) if values[j] < 0]
#print(value)
#X = modelrand(value, prob)
#print(X)


print(f'cos: {np.cos(data)}')
print(f'sin: {np.sin(data)}')
