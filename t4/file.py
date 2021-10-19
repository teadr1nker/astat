#!/usr/bin/python3
import pandas as pd
import numpy as np
from functions import *
import matplotlib.pyplot as plt

path = 'data.xlsx'
file = pd.ExcelFile(path)
sheets = file.sheet_names[1:]

#1
cortable = np.zeros((len(sheets), len(sheets)))
max = - 1.0
best = []
for i in range(len(sheets)):
    for j in range(i+1, len(sheets)):
        c = cor(sheets[i], sheets[j],
        parsesheet(file, sheets[i]), parsesheet(file, sheets[j]))
        cortable[i,j] = cortable[j, i] = c
        if c > max:
            best = [sheets[i], sheets[j]]
            max = c
print(cortable)
print(f'best: {best} with corvalue: {max}')
compare(parsesheet(file, best[0]), parsesheet(file, best[1]))

Y = file.sheet_names[0]

for sheet in sheets:
    #print(linreg(parsesheet(file, Y), parsesheet(file, sheet)))
    line = linreg(parsesheet(file, Y), parsesheet(file, sheet))
    x = parsesheet(file, Y)
    plt.plot(x, x * line.slope + line.intercept)

plt.show()
