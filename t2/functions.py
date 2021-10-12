import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import os, sys
sys.path.append('../common/')
from tex import tex

def parsesheet(file, sheet):
    tex.printline(f'Sheet: {sheet}')
    data1 = file.parse(sheet)
    res = []
    data1 = list(data1.to_numpy().T)
    for d1 in data1:
        data = []
        for d in d1:
            try:
                d = float(d)
                data.append(d)
            except:
                pass

        data = np.array(data)
        data = data[~pd.isnull(data)]
        res.append(data)
    return res

def testdistr(data, name ,a=0.1):
    res = stats.kstest(data, 'expon')
    tex.printline(f'kstes expon: {res[1]}')
    if res[1] > a:
        comparedistr(data, name+'_ks', 'expon')

    res = stats.kstest(data, 'norm')
    tex.printline(f'kstes norm: {res[1]}')
    if res[1] > a:
        comparedistr(data, name+'_ks', 'norm')

    res = stats.chisquare(data)
    tex.printline(f'chisquare norm: {res[1]}')
    if res[1] > a:
        comparedistr(data, name+'_ch', 'norm')

def cor(datax, datay, name, a=0.1):
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

    compare2(datax, datay, name)

def checkcor(a, crit):
    if a > crit[1]:
        tex.printline(f'Different')
    else:
        tex.printline(f'Dependant')

def kruskal3(data, name, a=0.1):
    if len(data) < 3:
        tex.printline('Data length must be 3 or greater')
        return
    kw = stats.kruskal(data[0], data[1], data[2])
    tex.printline(f'Kruskal-Wallis: {kw}')
    checkcor(a, kw)
    pf1 = probfunc(data[0])
    pf2 = probfunc(data[1])
    pf3 = probfunc(data[2])
    plt.plot(pf1[0], pf1[1])
    plt.plot(pf2[0], pf2[1])
    plt.plot(pf3[0], pf3[1])
    plt.title(name)
    plt.legend(['north', 'south', 'center'])
    filename = f'{name}.png'
    plt.savefig(filename)
    plt.clf()
    tex.addimage(filename)

def compare2(datax, datay, name, ns=True):
    pf1 = probfunc(datax)
    pf2 = probfunc(datay)
    plt.plot(pf1[0], pf1[1])
    plt.plot(pf2[0], pf2[1])
    #nbins = 10
    #c1, b1 = np.histogram(datax, bins=nbins)
    #plt.plot(b1[:-1], c1)
    #c2, b2 = np.histogram(datay, bins=nbins)
    #plt.plot(b2[:-1], c2)
    filename = f'compariosn_{name}.png'
    if ns:
        plt.legend(['north', 'south'])
    plt.title(name)
    plt.xlabel('prob')
    plt.ylabel('sample')
    plt.savefig(filename)
    plt.clf()
    tex.addimage(filename)

def probfunc(data):
    dict = {}
    for i in data:
        if i in dict:
            dict[i] += 1 / len(data)
        else:
            dict[i] = 1 / len(data)

    dict2 = {}
    for i in dict.keys():
        dict2[i] = 0
        for j in dict2.keys():
            dict2[i] += dict[j]

    return (sorted(dict2.keys()), sorted(dict2.values()))

def comparenorm(data, name):
    filename = f'norm{name}.png'
    nbins = 10
    c, b = np.histogram(data, bins=nbins)
    plt.plot(b[:-1], c)
    plt.title(name)
    plt.xlabel('sample')
    plt.ylabel('freq')
    #plt.plot(stats.norm.pdf(np.linspace(min(data), max(data), len(data))))
    plt.savefig(filename)
    plt.clf()
    tex.addimage(filename)

def compareexpon(data, name):
    filename = f'norm{name}.png'
    nbins = 10
    c, b = np.histogram(data, bins=nbins)
    plt.plot(b[:-1], c)
    #plt.plot(stats.norm.pdf(np.linspace(min(data), max(data), len(data))))
    plt.title(name)
    plt.xlabel('sample')
    plt.ylabel('freq')
    plt.savefig(filename)
    plt.clf()
    tex.addimage(filename)


def comparedistr(data, name, type='norm'):

    if type == 'norm':
        comparenorm(data, name)
    if type == 'expon':
        comparenorm(data, expon)
