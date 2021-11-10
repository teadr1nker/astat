#!/usr/bin/python3
import numpy as np
from functions import *
import os, sys
sys.path.append('../common/')


tex.printhead()

V = 18
X = np.loadtxt('First.txt', delimiter=' ')[:,V]
Y = np.loadtxt('Second.txt', delimiter=' ')[:,V]

dependency(X, Y)
cor('first', 'second', X, Y)

tex.printend()
