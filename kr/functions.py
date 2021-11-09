import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import os, sys
sys.path.append('../common/')
from tex import tex

def dependency(datax, datay, a=0.1):
    if len(datax) != len(datay):
        x = min([len(datax), len(datay)])
        datax = datax[:x]
        datay = datay[:x]
    tex.printline(f'a={a}')
    ks = stats.ks_2samp(datax, datay)
    tex.printline(f'Kolmogorov-Smirnov: {stats.ks_2samp(datax, datay)}')
    checkdep(a, ks[1])
    wil = stats.wilcoxon(datax, datay)
    tex.printline(f'Wilcoxon: {wil}')
    checkdep(a, wil[1])
    kw = stats.kruskal(datax, datay)
    tex.printline(f'Kruskal-Wallis: {kw}')
    checkdep(a, kw[1])

    compare2(datax, datay)

def checkdep(a, crit):
    if a > crit:
        tex.printline(f'Independent')
    else:
        tex.printline(f'Dependent')

def compare2(datax, datay, ns=True):
    nbins = 10
    c1, b1 = np.histogram(datax, bins=nbins)
    plt.plot(b1[:-1], c1)
    c2, b2 = np.histogram(datay, bins=nbins)
    plt.plot(b2[:-1], c2)
    filename = f'comparison.png'
    plt.legend(['First', 'Second'])
    plt.title('comparison')
    plt.xlabel('prob')
    plt.ylabel('sample')
    plt.savefig(filename)
    plt.clf()
    tex.addimage(filename)

def cor(name1, name2, datax, datay, a=0.05):
    #print(datax)
    m = min([len(datax), len(datay)])
    st, pv = stats.pearsonr(datax[:m], datay[:m])
    checkdep(a, pv)
    print(f'Spearman: {st}')
    st, pv = stats.kendalltau(datax[:m], datay[:m])
    checkdep(a, pv)
    print(f'Kendall: {st}')
    st, pv = stats.spearmanr(datax[:m], datay[:m])
    checkdep(a, pv)
    print(f'Spearman: {st}')
