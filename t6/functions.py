import pandas as pd
import numpy as np
from scipy import stats#, optimize
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

def dictstr2(dict):
    res = "{:<15} {:<10}\n".format('NAME', 'VALUE')
    for key, value in dict.items():
        val = value
        res += "{:<15} {:<10}\n".format(key, val)
    return res

def compare(datax, datay, a=0.1):
    if len(datax) != len(datay):
        x = min([len(datax), len(datay)])
        datax = datax[:x]
        datay = datay[:x]
    tex.printline(f'a={a}')
    ks = stats.ks_2samp(datax, datay)
    tex.plaintext(f'Kolmogorov-Smirnov: {stats.ks_2samp(datax, datay)}')
    checkcor(a, ks)
    wil = stats.wilcoxon(datax, datay)
    tex.plaintext(f'Wilcoxon: {wil}')
    checkcor(a, wil)
    kw = stats.kruskal(datax, datay)
    tex.plaintext(f'Kruskal-Wallis: {kw}')
    checkcor(a, kw)

def checkcor(a, crit):
    if a > crit[1]:
        tex.plaintext(f'Independent')
    else:
        tex.plaintext(f'Dependent')
