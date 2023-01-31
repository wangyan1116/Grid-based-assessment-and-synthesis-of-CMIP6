# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:31:29 2022

@author: wangyan
taking the precipitation as an example
"""

import os,glob
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt

file_path=r'H:\CMIP6_DATA\09_china_CMFD_linux\CMIP6\precipitation'
save_path=r'H:\CMIP6_DATA\09_china_CMFD_linux\CMIP6\std+corr+rmse+TSS'
cmfd=pd.read_csv(r'H:\CMIP6_DATA\09_china_CMFD_linux\CMIP6\CMFD\preicpitation.csv')
refsample=cmfd['CMFD']
files = os.listdir(file_path)
for f in files:
    Input_file = file_path  +'//'+ os.sep + f
    df = pd.read_csv(Input_file,index_col=False)
    name=os.path.splitext(f)[0]    
    sample=df['data']
    # print(sample.head())
    std = np.std(refsample)/np.std(sample)
    corr = np.corrcoef(refsample, sample)
    corr=corr[0]
    corr=corr[1]
    # print(corr)
    rmse=sqrt(mean_squared_error(refsample,sample))
    # print(rmse)  
    ##Taylor Skill Score,0:least skill,1:most skll
    TSS=4*((1+corr)**4)/(((std+1/std)**2)*(1+0.999)**4)
    data={'std':std,'corr':corr,'rmse':rmse,'TSS':TSS}
    # print(data)
    df1=pd.DataFrame(data,index=[name])
    # print(df1)
    output_file = save_path +'//'+'tas_41_std+corr+rmse+MCPI.csv'
    df1.to_csv(output_file,sep=',',header=False,mode='a')
    print(name+' is done')
print('ALL DONE') 