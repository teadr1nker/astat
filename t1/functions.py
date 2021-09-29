import pandas as pd
import numpy as np

def func(path, sname):
    file = pd.read_excel(path, sheet_name=sname)
    data = file.to_numpy().T[0]
    print('mean', data.mean())
    print('variance', data.var())
    print('std', data.std())

def parsesheet(file, sheet):
    #print(sheet)
    data = file.parse(sheet)
    data = list(data.to_numpy().T[0])
    for d in data:
        if not isinstance(d, np.floating):
            data.remove(d)
    data = np.array(data)
    data = data[~pd.isnull(data)]
    return data

def func2(data):
    print('mean', data.mean())
    print('variance', data.var())
    print('std', data.std())
