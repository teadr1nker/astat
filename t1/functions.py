import pandas as pd
import numpy as np

def func(path, sname):
    file = pd.read_excel(path, sheet_name=sname)
    data = file.to_numpy().T[0]
    print('mean', data.mean())
    print('variance', data.var())
    print('std', data.std())
