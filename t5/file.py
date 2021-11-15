#!/usr/bin/python3
import pandas as pd
import numpy as np
from functions import *
import sys
sys.path.append('../common/')
from tex import tex
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols


filename = 'data3.csv'
df = pd.read_csv(filename, sep=',', encoding = "utf-8")
print(df)
ax = sns.boxplot(x='side', y='value', data=df, color='#99c2a2')
ax = sns.swarmplot(x="side", y="value", data=df, color='#7d0013')
#plt.show()
model = ols('value ~ C(side)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)
model = ols('value ~ C(side) + C(space) + C(side):C(space)', data=df).fit()
print(sm.stats.anova_lm(model, typ=2))
