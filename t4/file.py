#!/usr/bin/python3
import pandas as pd
import numpy as np
from functions import *
import matplotlib.pyplot as plt

path = 'data.xlsx'
file = pd.ExcelFile(path)
sheets = file.sheet_names[1:]

#1
cortable = np.ones((len(sheets), len(sheets)))
max = -1.0
best = []
for i in range(len(sheets)):
    for j in range(i+1, len(sheets)):
        c = cor(sheets[i], sheets[j],
        parsesheet(file, sheets[i]), parsesheet(file, sheets[j]))
        cortable[i,j] = cortable[j, i] = c
        if abs(c) > max:
            best = [sheets[i], sheets[j]]
            max = abs(c)
print(cortable)
print(f'best: {best} with corvalue: {max}')
compare(parsesheet(file, best[0]), parsesheet(file, best[1]))

Y = file.sheet_names[0]

for sheet in sheets:
    #print(linreg(parsesheet(file, Y), parsesheet(file, sheet)))
    line = linreg(parsesheet(file, Y), parsesheet(file, sheet))
    x = parsesheet(file, Y)
    plt.plot(x, x * line.slope + line.intercept)

plt.legend(sheets)
#plt.show()
plt.clf()

x = parsesheet(file, sheets[2])
y = parsesheet(file, Y)

lreg = logreg(x, y)
g = sorted(np.log(x) * lreg[0] + lreg[1])
#plt.plot(sorted(x), g / max(g))
ereg = expreg(x, y)
#plt.plot(sorted(x), sorted(np.exp(x * ereg[1]) * ereg[0]))

#plt.legend(['log', 'exp'])
#plt.show()
