import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import os

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

def func(data, name):
    print(f'mean: {data.mean()}')
    print(f'variance: {data.var()}')
    print(f'std: {data.std()}')
    for n in range(1, 5):
        print(f'beginning moment n = {n}: {np.mean(data**n)}')
        print(f'central moment n = {n}: {stats.moment(data, n)}')
    print(f'skewness: {stats.skew(data)}')
    print(f'median: {np.median(data)}')
    print(f'kurtosis: {stats.kurtosis(data, fisher=False)}')

    nbins = 10
    dataMid = (max(data) - min(data))/1
    c, b = np.histogram(data, bins=nbins)
    plt.plot(b[:-1], c)
    plt.hist(data, bins=nbins)
    plt.title(name)
    plt.xlabel('sample')
    plt.ylabel('frequency')
    plt.savefig(f'hist_{name}.png')
    plt.clf()
    print(f'file://{os.path.abspath(f"hist_{name}.png")}')

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

    plt.plot(sorted(dict2.keys()), sorted(dict2.values()))
    plt.title(name)
    plt.xlabel('sample')
    plt.ylabel('prob')
    plt.savefig(f'probFunc_{name}.png')
    plt.clf()
    print(f'file://{os.path.abspath(f"probFunc_{name}.png")}')

    print('interval 95%: {}'.format(
    stats.t.interval(0.95, len(data)-1, loc=np.mean(data),scale=stats.sem(data))
    ))
    print('interval 99%: {}'.format(
    stats.t.interval(0.99, len(data)-1, loc=np.mean(data),scale=stats.sem(data))
    ))
