import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import os

def parsesheet(file, sheet):
    #print(sheet)
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
    for n in range(4):
        print(f'central moment n = {n+1}: {stats.moment(data, n+1)}')
    print(f'skewness: {stats.skew(data)}')
    print(f'median: {np.median(data)}')
    print(f'kurtosis: {stats.kurtosis(data, fisher=False)}')

    plt.hist(data)
    plt.savefig(f'hist_{name}.png')
    plt.clf()
    print('interval 95%: {}'.format(
    stats.t.interval(0.95, len(data)-1, loc=np.mean(data),scale=stats.sem(data))
    ))
    print('interval 99%: {}'.format(
    stats.t.interval(0.99, len(data)-1, loc=np.mean(data),scale=stats.sem(data))
    ))
