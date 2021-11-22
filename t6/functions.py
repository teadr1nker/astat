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
