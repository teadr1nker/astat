#!/usr/bin/python3
import pandas as pd
import numpy as np
from functions import *
path = 'data.xlsx'
file = pd.ExcelFile(path)
for sheet in file.sheet_names:
    data = parsesheet(file, sheet)
    print(f'sheet: {sheet}')
    func(data, sheet)
    print()
