#!/usr/bin/python3
import numpy as np
from functions import *
import os, sys
sys.path.append('../common/')

tex.printhead()
tex.section('Контрольная работа Миролюбов АК 22404')

V = 18
X = np.loadtxt('First.txt', delimiter=' ')[:,V]
Y = np.loadtxt('Second.txt', delimiter=' ')[:,V]

tex.section('Однородность', 1)
dependency(X, Y)
tex.section('Корреляция', 1)
cor('first', 'second', X, Y)

tex.printend()
