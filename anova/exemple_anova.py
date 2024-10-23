# -*- coding: utf-8 -*-
"""
anova graph for energy security in a cliamte constrained world
"""


import pandas as pd
from pandas import DataFrame,read_csv,concat,notnull
import glob
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import numpy as np
            

colors = ["#8dd3c7","#ffffb3","#bebada","#fb8072","#80b1d3","#fdb462","#b3de69"]
columns=['Residual','ind_ssp','ind_EEI','ind_technoelec','ind_technoCCS','ind_technoenduses','ind_ffuels']
legends=['interactions of drivers','growth','IEE','techno_electricity','techno_CCS','techno_end uses','fossil_fuels']

IEeur=read_csv('IEeur.tsv')
IEeur=IEeur.astype(float)  

out=DataFrame()
outpc=DataFrame()

for year in range(21,76):
    formula="IEeur{} ~ ind_ssp+ind_EEI+ind_technoelec+ind_technoCCS+ind_technoenduses+ind_ffuels".format(year)
    olsmodel=ols(formula,data=IEeur).fit()
    table=anova_lm(olsmodel)
    table['sum_sq_pc']=100*table['sum_sq']/table['sum_sq'].sum()
    #out=out.append(table['sum_sq'],ignore_index=True)
    #outpc=outpc.append(table['sum_sq_pc'],ignore_index=True)
    out=pd.concat( [out,table['sum_sq']],ignore_index=True, axis=1)
    outpc=pd.concat( [outpc,table['sum_sq']],ignore_index=True, axis=1)

out = out.transpose()
outpc = outpc.transpose()

out.index=list(range(2020,2075))
outpc.index=list(range(2020,2075))


font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 15}
plt.rc('font', **font)
plt.figure(figsize=(8,6))
ax=plt.subplot(111)


prev=0*out['Residual']
i=0
for thecol in columns:
    plt.plot(outpc.index,prev+outpc[thecol],color=colors[i])
    ax.fill_between(outpc.index, prev, prev+outpc[thecol],facecolor=colors[i],alpha=0.9)    
    
    if legends[i] in ['techno_end uses','techno_electricity','growth']:
        ymean=(prev[2021]+prev[2021]+outpc.loc[2021,thecol])/2
        plt.annotate(legends[i], xy=(2020, ymean),  xycoords='data',
                        xytext=(50, 10), textcoords='offset points',
                        arrowprops=dict(arrowstyle="fancy",
                                        fc=colors[i], ec='black',
                                        patchB=None,
                                        connectionstyle="angle3,angleA=0,angleB=60"),
                            )
    else:
        ymean=(prev[2074]+prev[2074]+outpc.loc[2074,thecol])/2
        plt.annotate(legends[i], xy=(2075, ymean),  xycoords='data',
                    xytext=(50, 10), textcoords='offset points',
                    arrowprops=dict(arrowstyle="fancy",
                                    fc=colors[i], ec=colors[i],
                                    patchB=None,
                                    connectionstyle="angle3,angleA=0,angleB=60"),
                        )
        
    prev+=outpc[thecol]
    i+=1

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#ax.set_yticklabels([])
ax.set_ylim([0,100])
plt.ylabel("Fraction of total variance")
#plt.title("% of variance of energy intensity of GDP explained by each driver.", y=1.08)
plt.savefig('IEeurANOVA.png',bbox_inches="tight",dpi=300)

