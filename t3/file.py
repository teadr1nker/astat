#!/usr/bin/python3
#import pandas as pd
import numpy as np
import scipy as sp
from scipy import stats
#from scipy import optimize
import matplotlib.pyplot as plt
import os, sys, inspect
sys.path.append('../common/')
from tex import tex

def density(data, n):
    c, b = np.histogram(data, bins=n)
    return (b[:-1], c)

def montecarloint(func, N, a, b):
    res = 0.0
    X = np.linspace(a, b, N)
    for i in range(N):
        res+= func(X[i])

    return ((b - a)/ N) * res

def montecarlomax(func, N, a, b):
    X = np.random.uniform(a, b, N)
    max = -np.inf
    x = 0.0
    for i in range(N):
        y = func(X[i])
        if y > max:
            max = y
            x = X[i]
    return (max, x)

tex.printhead()
tex.section('Статистическое моделирование')
#1
N = 100
a = 0.0
b = 1.0
tex.section(f'Равномерное распределение [{a}:{b}]',1)
tex.printline(F'N={N} a={a} b={b}')
data1 = np.random.uniform(a, b, N)
plt.hist(data1, 10)
plt.title(f'uniform [{a}:{b}]')
plt.xlabel('sample')
plt.ylabel('freq')
plt.savefig('uniform1.png')
plt.clf()
tex.addimage('uniform1.png')

#2
N = 100
a = 2.0
b = 7.0
tex.section(f'Равномерное распределение [{a}:{b}]',1)
data2 = np.random.uniform(a, b, N)
#print(data1)
tex.printline(F'N={N} a={a} b={b}')
plt.hist(data2, 20)
plt.title(f'uniform [{a}:{b}]')
plt.xlabel('sample')
plt.ylabel('freq')
plt.savefig('uniform2.png')
plt.clf()
tex.addimage('uniform2.png')

#3
N = 100
mean = 6
var = 200
tex.section('Нормальное распределение', 1)
tex.printline(F'N={N}')
data3 = np.random.normal(mean, var, N)
#norm = stats.norm.rvs(mean, var, N)
#dens = density(norm, 20)
plt.hist(data3, 20)
plt.title(f'norm mean={mean} var={var}')
#plt.plot(dens[0], dens[1])c
plt.xlabel('sample')
plt.ylabel('freq')
plt.savefig('norm.png')
plt.clf()
tex.addimage('norm.png')

#4
N = 100
lmbd = 2
tex.section('Экспоненциальное', 1)
tex.printline(F'N={N}')
data4 = np.random.exponential(1/lmbd, N)
plt.hist(data4, 20)
plt.title(f'exponential lambda={lmbd}')
plt.xlabel('sample')
plt.ylabel('freq')
plt.savefig('expon.png')
plt.clf()
tex.addimage('expon.png')

#5
N = 200
a = 10
b = 30
tex.section('Вычисление определенного интеграла методом Монте-Карло', 1)
tex.printline(f'Ограничения [{a}:{b}]')
f = lambda x: -((x - 15) ** 2 - 100)
tex.printline(inspect.getsource(f))
plt.plot(np.linspace(a,b,N), [f(x) for x in np.linspace(a,b,N)])
plt.title('function')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('function.png')
tex.addimage('function.png')
tex.printline(f'Monte Carlo N = {N}: {montecarloint(f, N, a, b)}')
tex.printline(f'Monte Carlo N = {N*10}: {montecarloint(f, N*10, a, b)}')
tex.printline(f'scipy.integrate.quad(): {sp.integrate.quad(f, a, b)[0]}')

#6
tex.section('Определение экстремума функции методом Монте-Карло', 1)
y, x = montecarlomax(f, N, a, b)
tex.printline(f'Monte Carlo N={N}: max={y} at x = {x}')
plt.plot([x], [y], marker='o')
plt.savefig('max.png')
tex.addimage('max.png')


tex.printend()
