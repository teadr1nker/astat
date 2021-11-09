#!/usr/bin/python3
import numpy as np
from functions import *

V = 18
X = np.loadtxt('First.txt', delimiter=' ')[:,V]
Y = np.loadtxt('Second.txt', delimiter=' ')[:,V]

dependency(X, Y)
