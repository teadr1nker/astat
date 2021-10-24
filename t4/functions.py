import pandas as pd
import numpy as np
from scipy import stats, optimize
import matplotlib.pyplot as plt
import os, sys#, inspect
sys.path.append('../common/')
from tex import tex

def parsesheet(file, sheet):
    data1 = file.parse(sheet)
    data1 = list(data1.to_numpy().T[0])
    data = []
    for d in data1:
        try:
            d = float(d)
            data.append(d)
        except:
            pass

    data = np.array(data)
    data = data[~pd.isnull(data)]
    return data

def cor(name1, name2, datax, datay, a=0.05):
    #print(datax)
    m = min([len(datax), len(datay)])
    st, pv = stats.pearsonr(datax[:m], datay[:m])
    if pv > a:
        plt.scatter(datax[:m] / max(datax), datay[:m] / max(datay))
        filename = f'scatter{name1}_{name2}.png'
        plt.title(f'scatter: {name1}/{name2}')
        plt.savefig(filename)
        tex.addimage(filename)
        plt.clf()
    return (round(st, 4))

def compare(datax, datay, a=0.1):
    if len(datax) != len(datay):
        x = min([len(datax), len(datay)])
        datax = datax[:x]
        datay = datay[:x]
    tex.printline(f'a={a}')
    ks = stats.ks_2samp(datax, datay)
    tex.printline(f'Kolmogorov-Smirnov: {stats.ks_2samp(datax, datay)}')
    checkcor(a, ks)
    wil = stats.wilcoxon(datax, datay)
    tex.printline(f'Wilcoxon: {wil}')
    checkcor(a, wil)
    kw = stats.kruskal(datax, datay)
    tex.printline(f'Kruskal-Wallis: {kw}')
    checkcor(a, kw)


def checkcor(a, crit):
    if a > crit[1]:
        tex.printline(f'Different')
    else:
        tex.printline(f'Dependant')

def linreg(datax, datay):
    m = min([len(datax), len(datay)])
    return stats.linregress(datax[:m], datay[:m])

def logreg(x, y):
    m = min([len(x), len(y)])
    x = x[:m]; y = y[:m]
    return np.polyfit(np.log(x), y, 1)

def expreg(x, y):
    m = min([len(x), len(y)])
    x = x[:m]; y = y[:m]
    return np.polyfit(x, np.log(y), 1)

def powreg(x, y):
    m = min([len(x), len(y)])
    x = x[:m]; y = y[:m]
    popt, pcov = optimize.curve_fit(lambda fx,a,b: a*fx**-b,  y,  x)
    return popt
