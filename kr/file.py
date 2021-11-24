#!/usr/bin/python3
import numpy as np
from functions import *
import os, sys
sys.path.append('../common/')
import matplotlib.pyplot as plt

tex.printhead()
tex.section('Контрольная работа Миролюбов АК 22404')

V = 19#18
X = np.loadtxt('First.txt', delimiter=' ')[:,V]
Y = np.loadtxt('Second.txt', delimiter=' ')[:,V]

tex.section('Однородность', 1)
dependency(X, Y)
tex.section('Корреляция', 1)
cor('first', 'second', X, Y)
tex.section('Линейная регрессия', 1)
linreg(X, Y)
tex.section('Моделирование СВ',1)

x1=-V
x2=V
x3=V**2+1

p1=1/(V+1)
p2=max([1/((V+1)**2),0.1])
p3 = 1 - p1 - p2
values = [x1, x2, x3]
tex.printline('Закон распределения')
probs = [p1, p2, p3]
tex.plaintext(f'Вероятности: {np.round(probs, 4)}\nЗначения: {values}')
data = modelrand(values, probs, 100)
plt.hist(data)
plt.xlabel('sample')
plt.ylabel('freq')
plt.title('Гистограмма частот')
plt.savefig('hist2.png')
tex.addimage('hist2.png')

tex.printline('Моделирование событий')
for d in data:
    if d < 0:
        p = findprob(values, probs, d)
        tex.printline(f'Событие X<0 X={d}, с вероятностью {round(p, 4)}')
        break
E = data.mean()
for d in data:
    X1 = d
    if X1 > E:
        for d in data:
            X2 = d
            if X1 + X2 < 2*E:
                p1 = findprob(values, probs, X1)
                p2 = findprob(values, probs, X2)
                tex.printline('2 случайных события {X1+X2<2EX} и {X1>EX} при E'
                      + f'={E} ({X1},{X2}), с вероятностью {round(p1 * p2, 4)}')
                break
        break


tex.printline(f'cos: {np.cos(modelrand(values, probs, 1))[0]}')
tex.printline(f'sin: {np.sin(modelrand(values, probs, 1))[0]}')
tex.printend()
