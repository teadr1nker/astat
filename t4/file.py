#!/usr/bin/python3
import pandas as pd
import numpy as np
from functions import *
import matplotlib.pyplot as plt
sys.path.append('../common/')
from tex import tex

tex.printhead()
path = 'data.xlsx'
file = pd.ExcelFile(path)
sheets = file.sheet_names[1:]
tex.section('Корреляционный и регрессионный анализ')
#1
tex.section('Корреляционная матрица и рассеивание' ,1)
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
tex.section('Проверка лучших', 1)
#print(cortable)
tex.printline(f'{sheets}')
tex.addtable(cortable, 'correlation')
tex.printline(f'best: {best} with corvalue: {max}')
compare(parsesheet(file, best[0]), parsesheet(file, best[1]))

Y = file.sheet_names[0]
tex.section('Линейная регрессия' ,1)
for sheet in sheets:
    #print(linreg(parsesheet(file, Y), parsesheet(file, sheet)))
    line = linreg(parsesheet(file, Y), parsesheet(file, sheet))
    x = parsesheet(file, Y)
    plt.plot(x, x * line.slope + line.intercept)

plt.legend(sheets)
plt.title(f'linear regression: {Y}/rest')
plt.savefig('linreg.png')
tex.addimage('linreg.png')
plt.clf()

tex.section('Логарифмическая, степенная, показательная регрессия' ,1)
x = parsesheet(file, sheets[2])
y = parsesheet(file, Y)

m = min([len(x), len(y)])
plt.plot(sorted(x[:m]), sorted(y[:m] / np.max(y)))

lreg = logreg(x, y)
g = np.log(x) * lreg[0] + lreg[1]
g = sorted(g) / np.max(g)
plt.plot(sorted(x), g)

ereg = expreg(x, y)
g = np.exp(ereg[1] + ereg[0] * x)
g = sorted(g) / np.max(g)
plt.plot(sorted(x), g)

preg = powreg(x, y)
g = preg[0]*x**-preg[1]
g = sorted(g) / np.max(g)
plt.plot(sorted(x), g)

plt.legend(['orig', 'log', 'exp', 'pow'])
plt.title(f'regression: {sheets[2]}/{Y}')
filename = f'{sheets[2]}_{Y}_regression.png'
plt.savefig(filename)
tex.addimage(filename)
tex.printend()
