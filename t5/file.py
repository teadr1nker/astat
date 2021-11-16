#!/usr/bin/python3
import pandas as pd
import numpy as np
#from functions import *
import sys
sys.path.append('../common/')
from tex import tex
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

tex.printhead()
filename = 'data3.csv'
df = pd.read_csv(filename, sep=',', encoding = "utf-8")
#print(df)
ax = sns.boxplot(x='side', y='value', data=df, color='green')
#ax = sns.swarmplot(x="side", y="value", data=df, color='red')
plt.savefig('img.png')
tex.addimage('img.png')
ax = sns.boxplot(x='space', y='value', data=df, color='green')
plt.savefig('img2.png')
tex.addimage('img2.png')
model = ols('value ~ C(side)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
tex.plaintext(anova_table)
model = ols('value ~ C(side) + C(space)', data=df).fit()
tex.plaintext(sm.stats.anova_lm(model, typ=2))
model = ols('value ~ C(side):C(space)', data=df).fit()
tex.plaintext(sm.stats.anova_lm(model, typ=2))
tex.printend()
