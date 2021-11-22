#!/usr/bin/python3
import pandas as pd
import numpy as np
from functions import *
import sys
sys.path.append('../common/')
from tex import tex
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


filename = '../t4/data.xlsx'
file = pd.ExcelFile(filename)
sheets = file.sheet_names[1:]

data = [parsesheet(file, sheet) for sheet in sheets]
m = min([len(d) for d in data])
data = [d[:m] for d in data]
#print(data)

for d in data:
    plt.plot(d)
plt.legend(sheets)
#plt.show()

pca = PCA()
pca.fit(data)
print(np.round(pca.explained_variance_ratio_, 5))
print([round(x) for x in pca.singular_values_])     #not working properly
plt.plot(sheets ,pca.singular_values_)
plt.xlabel('eingvalues')
plt.ylabel('value')
#plt.show()
for d in pca.fit_transform(data):
    plt.plot(d)
plt.legend(sheets)
#plt.show()
plt.clf()
print(pca.explained_variance_)
#print(pca.n_features_in_)


dataY = [parsesheet(file, sheet) for sheet in file.sheet_names]
m = min([len(d) for d in dataY])
dataY = [d[:m] for d in dataY]
pca = PCA()
pca.fit(dataY)
print(np.round(pca.explained_variance_ratio_, 5))
print([round(x) for x in pca.singular_values_])
plt.plot(file.sheet_names ,pca.singular_values_)
plt.show()
plt.clf()
