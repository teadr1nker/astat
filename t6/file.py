#!/usr/bin/python3
import pandas as pd
import numpy as np
from functions import *
import sys
sys.path.append('../common/')
from tex import tex
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

tex.printhead()
tex.section('Компонентный анализ')
filename = '../t4/data.xlsx'
file = pd.ExcelFile(filename)
sheets = file.sheet_names[1:]

data = [parsesheet(file, sheet) for sheet in sheets]
m = min([len(d) for d in data])
data = [d[:m] for d in data]
#print(data)
tex.section('Анализ данных')
for d in data:
    plt.plot(d)
plt.legend(sheets)
plt.title('Uncompressed data')
plt.savefig('data.png')
tex.addimage('data.png')
plt.clf()

pca = PCA()
pca.fit(data)
tex.printline('Важность')
tex.plaintext(dictstr2(dict(zip(sheets,
np.round(pca.explained_variance_ratio_, 5)))))
tex.printline('Вклады в суммарную дисперсию')
tex.plaintext(dictstr2(dict(zip(sheets,
[round(x) for x in pca.singular_values_]))))     #not working properly
plt.plot(sheets ,pca.singular_values_)
plt.xticks(sheets, rotation='vertical')
plt.subplots_adjust(bottom=0.3)
plt.xlabel('eingvalues')
plt.ylabel('value')
plt.savefig('vals1.png')
tex.addimage('vals1.png')
plt.clf()

for d in pca.fit_transform(data):
    plt.plot(d)
plt.legend(sheets)
plt.title('Compressed data')
plt.savefig('compressed.png')
tex.addimage('compressed.png')
plt.clf()
tex.plaintext(dictstr2(dict(zip(sheets,
[round(x) for x in pca.explained_variance_]))))
#print(pca.n_features_in_)


#print(pca.score(data))
#print(np.round(pca.explained_variance_ratio_, 5))

tex.section('Анализ cвязи с Y')

dataY = [parsesheet(file, sheet) for sheet in file.sheet_names]
m = min([len(d) for d in dataY])
dataY = [d[:m] for d in dataY]
pca = PCA()
pca.fit(dataY)
tex.printline('Важность')
tex.plaintext(dictstr2(dict(zip(file.sheet_names,
np.round(pca.explained_variance_ratio_, 5)))))
tex.printline('Вклады в суммарную дисперсию')
tex.plaintext(dictstr2(dict(zip(file.sheet_names,
[round(x) for x in pca.singular_values_]))))
plt.plot(file.sheet_names ,pca.singular_values_)
plt.xticks(file.sheet_names, rotation='vertical')
plt.subplots_adjust(bottom=0.3)
plt.savefig('vals2.png')
tex.addimage('vals2.png')
plt.clf()
tex.printline('Зависимость')
compare(dataY[0], dataY[1])


tex.printend()
