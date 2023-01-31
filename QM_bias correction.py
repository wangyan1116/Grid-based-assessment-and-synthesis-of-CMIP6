# -*- coding: utf-8 -*-
"""
Created on Tue May 31 08:27:14 2022

@author: wangyan
taking the precipitation as example
"""

import os,glob
import xarray as xr
from xclim import sdba
import pandas as pd
import numpy as np
file_path='/data/CMIP6/pr/historical'
file_path126='/data/CMIP6/pr/ssp126'
file_path245='/data/CMIP6/pr/ssp245'
file_path585='/data/CMIP6/pr/ssp585'
save_pathhis='/data/CMIP6/QM_nc/pr/historical'
save_path126='/data/CMIP6/QM_nc/pr/ssp126'
save_path245='/data/CMIP6/QM_nc/pr/ssp245'
save_path585='/data/CMIP6/QM_nc/pr/ssp585'


save_pathhis_csv='/data/CMIP6/QM_csv/pr/historical'
save_path126_csv='/data/CMIP6/QM_csv/pr/ssp126'
save_path245_csv='/data/CMIP6/QM_csv/pr/ssp245'
save_path585_csv='/data/CMIP6/QM_csv/pr/ssp585'

ref1=xr.open_dataset('/data/CMIP6/CMFD/0.5C_prec_CMFD_V0106_B-01_01mo_010deg_197901-201812.nc')
ref=ref1['prec']
model=pd.read_csv('/data/CMIP6/model.csv')
print(model)
for m in model['model']:
    print(m)
    file_name= m
    # print(file_name)
    Input_file = file_path + os.sep + file_name+'.nc'
    df_hist = xr.open_dataset(Input_file)
    # print(df_hist)    
    date=df_hist['time']
    time_tmp1 = df_hist.indexes['time']
    # print(time_tmp1)
    time_tmp2 = []
    for t in list(time_tmp1):
        # print(i)
        a=t.year
        b=t.month
        time_tmp2.append(pd.to_datetime('{}/{}'.format(a,b),format='%Y/%m'))
    df_hist = df_hist.assign_coords(time = time_tmp2)
    # print(df_hist.indexes['time']) 
    
    df_hist['time'] = np.sort(df_hist['time'].values)
    # print(df_hist['time'])
    hist=df_hist['pr'].loc['1979-01-01':'2014-12-31']
    # print(hist)
 ####-------------------------------------------------------####
        
    Input_file126 = file_path126 + os.sep + file_name+'.nc'
    # print(Input_file126)
    df_sim126 = xr.open_dataset(Input_file126)
    
    date126=df_sim126['time']
    time_tmp126_1 = df_sim126.indexes['time']
    # print(time_tmp126)
    time_tmp126_2 = []
    for t126 in list(time_tmp126_1):
        # print(i)
        a126=t126.year
        b126=t126.month
        time_tmp126_2.append(pd.to_datetime('{}/{}'.format(a126,b126),format='%Y/%m'))
    df_sim126 = df_sim126.assign_coords(time = time_tmp126_2)
    # print(df_sim126.indexes['time']) 
    sim126=df_sim126['pr']
    # print(df_sim126['pr'])
    
 ####-------------------------------------------------------####    
    Input_file245 = file_path245 + os.sep + file_name+'.nc'
    df_sim245 = xr.open_dataset(Input_file245)
    date245=df_sim245['time']
    time_tmp245_1 = df_sim245.indexes['time']
    # print(time_tmp245_1)
    time_tmp245_2 = []
    for t245 in list(time_tmp245_1):
        # print(i)
        a245=t245.year
        b245=t245.month
        time_tmp245_2.append(pd.to_datetime('{}/{}'.format(a245,b245),format='%Y/%m'))
    df_sim245 = df_sim245.assign_coords(time = time_tmp245_2)
    # print(df_hist.indexes['time']) 
    sim245=df_sim245['pr']    
    # print(df_sim245['pr'])
    
  ####-------------------------------------------------------####   
    Input_file585 = file_path585 + os.sep + file_name+'.nc'
    df_sim585 = xr.open_dataset(Input_file585)     
    
    date585=df_sim585['time']
    time_tmp585_1 = df_sim585.indexes['time']
    # print(time_tmp585_1)
    time_tmp585_2 = []
    for t585 in list(time_tmp585_1):
        # print(i)
        a585=t585.year
        b585=t585.month
        time_tmp585_2.append(pd.to_datetime('{}/{}'.format(a585,b585),format='%Y/%m'))
    df_sim585 = df_sim585.assign_coords(time = time_tmp585_2)
    # print(df_hist.indexes['time']) 
    sim585=df_sim585['pr']
    # print(sim585)
    
    dqm = sdba.adjustment.DetrendedQuantileMapping.train(ref, hist)##QM    
    scen = dqm.adjust(hist)
    # print(scen)
    scen126 = dqm.adjust(sim126)
    scen245 = dqm.adjust(sim245)
    scen585 = dqm.adjust(sim585)
    
    output_file = save_pathhis + os.sep + file_name+'_scen.nc'
    # print(output_file)
    scen.to_netcdf(output_file)    
    df=scen.to_dataframe()    
    output_file_csv = save_pathhis_csv+'//' + file_name+'.csv'
    # print(output_file_csv)
    df.to_csv(output_file_csv,sep=',',index=True,header=True)
    # print(file_name +'DONE')
    
    output_file126 = save_path126 + os.sep + file_name+'_scen.nc'
    scen126.to_netcdf(output_file126)
    # print(output_file126)
    df126=scen126.to_dataframe()    
    output_file126_csv = save_path126_csv+'//' + file_name+'.csv'
    df126.to_csv(output_file126_csv,sep=',',index=True,header=True)
    # print(output_file126_csv)
    # print(file_name126 +'DONE')
    
    output_file245 = save_path245 + os.sep + file_name+'_scen.nc'
    scen245.to_netcdf(output_file245)
    # print(output_file245)
    df245=scen245.to_dataframe()    
    output_file245_csv = save_path245_csv+'//' + file_name+'.csv'
    # print(output_file245_csv)
    df245.to_csv(output_file245_csv,sep=',',index=True,header=True)
    # print(file_name245 +'DONE')
    
    output_file585 = save_path585 + os.sep + file_name+'_scen.nc'
    scen585.to_netcdf(output_file585)  
    # print(output_file585)
    df585=scen585.to_dataframe()    
    output_file585_csv = save_path585_csv+'//' + file_name+'.csv'
    # print(output_file585_csv)
    df585.to_csv(output_file585_csv,sep=',',index=True,header=True)
    print(file_name +'DONE')
    
print('ALL DONE')
