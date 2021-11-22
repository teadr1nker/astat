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
    tex.printline(f'Значимость a={a}')
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
    #tex.printline(f'pvalue={crit}')
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
    plt.xlabel('sample')
    plt.ylabel('freq')
    plt.savefig(filename)
    plt.clf()
    tex.addimage(filename)

def cor(name1, name2, datax, datay, a=0.1):
    #print(datax)
    tex.printline(f'Значимость a={a}')
    m = min([len(datax), len(datay)])
    st, pv = stats.pearsonr(datax[:m], datay[:m])
    tex.printline(f'Pearson: cor={st}, pv={pv}')
    checkdep(a, pv)
    st, pv = stats.kendalltau(datax[:m], datay[:m])
    tex.printline(f'Kendall: cor={st}, pv={pv}')
    checkdep(a, pv)
    st, pv = stats.spearmanr(datax[:m], datay[:m])
    tex.printline(f'Spearman: cor={st}, pv={pv}')
    checkdep(a, pv)

################################################################################

def linreg(X, Y, a=0.1):
    tex.printline('Y = X * A + B')
    A, B, rv, pv, _ = stats.linregress(X, Y)
    tex.printline(f'A={A}, B={B}')
    plt.scatter(X, Y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(X, X * A + B, color='orange')
    plt.legend(['regression line', 'scatter plot'])
    plt.savefig('scatter.png')
    tex.addimage('scatter.png')
    plt.clf()
    tex.printline(f'Коэффициент детерминации Rvalue={rv}')
    tex.printline(f'Pvalue={pv}')
    tex.printline(f'Значимость а={a}')
    if a > pv:
        tex.printline('Не значима, pv < a')
    else:
        tex.printline('Значима, pv > a')
    plt.hist(Y - X * A + B)
    plt.title('Гистограмма остатков')
    plt.xlabel('sample')
    plt.ylabel('freq')
    plt.savefig('hist.png')
    tex.addimage('hist.png')
    plt.clf()
    plt.plot(sorted(Y), sorted(X * A + B))
    plt.xlabel('Y')
    plt.ylabel('f(X)')
    plt.title('Зависимость')
    plt.savefig('dependency2.png')
    tex.addimage('dependency2.png')
    plt.clf()

def modelrand(values, probs, n=10):
    if len(values) != len(probs):
        return None
    res = []
    #print(values, probs)
    for i in range(n):
        rnd = np.random.uniform()
        prob = 0.0
        val = values[-1]
        for j in range(len(probs) - 1):
            prob += probs[j]
            if prob > rnd:
                val = (values[j])
                break
        res.append(val)
    return np.array(res)
