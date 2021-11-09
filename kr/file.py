#!/usr/bin/python3
import numpy as np

V = 18
X = np.loadtxt('First.txt', delimiter=' ')[:,V]
Y = np.loadtxt('Second.txt', delimiter=' ')[:,V]

print(Y)
