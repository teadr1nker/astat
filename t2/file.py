#!/usr/bin/python3
import pandas as pd
import numpy as np
from functions import *
import sys
sys.path.append('../common/')
from tex import tex

path1 = '../t1/data.xlsx'
path2 = 'data.xlsx'
file = pd.ExcelFile(path1)

#1
#data = parsesheet(file, 'ZhKH')
#test1(data)
tex.printhead()
for sheet in file.sheet_names:
    testdistr(parsesheet(file, sheet)[0], sheet)

file = pd.ExcelFile(path2)
for sheet in file.sheet_names:
    data = parsesheet(file, sheet)
    cor(data[0], data[1], sheet)

kruskal3(parsesheet(file, file.sheet_names[2]), file.sheet_names[2])
tex.printend()
