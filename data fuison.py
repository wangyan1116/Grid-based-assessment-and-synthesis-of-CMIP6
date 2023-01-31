# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 10:18:28 2022

@author: dell
"""
import os,glob
import pandas as pd
import pandas as pd
model_path="/data/CMIP6/05_QM_dorpnull"
save_path="/data/CMIP6/09_QM_TOP5/41"
lat_lon_path='/data/CMIP6/08_TSS_weight/41'
var=['pr','tas']
for v in var:
    print(v)
    lat_lon_path1=lat_lon_path+'/'+v
    files = os.listdir(lat_lon_path1)
    ssp=['historical','ssp126','ssp245','ssp585']    
    for s in ssp:
        # print(s)        
        for f in files:
            Input_file = lat_lon_path1+ os.sep + f
            # print(Input_file)
            lat_lon=os.path.splitext(f)[0]
            # print(lat_lon)
            df = pd.read_csv(Input_file,index_col=False)
            df=df.rename(columns={'Unnamed: 0':'model'})
            # print(df)
            model=df['model']
            for m in model:
                # print(m)
                Input_file_m=model_path+'/'+v+'/'+s+'/'+m+'.csv'
                # print(Input_file_m)
                df_m=pd.read_csv(Input_file_m,index_col=False)
                # print(df_m)
                df_1=df_m[df_m['lat_lon']==lat_lon]
                df_1['model']=m
                # print(df_1)
                df_2=pd.merge(df_1,df,on=['model'],how='left')
                # print(df_2)
                df_2[m]=df_2['scen']*df_2[lat_lon] 
                df_2=df_2.drop(columns=['lat_lon','scen',lat_lon])
                # print(df_2)        
                output_file = save_path+'/'+v+'/'+s +'/'+ lat_lon +'.csv' 
                # print(da)
                df_2.to_csv(output_file,sep=',',index=False,header=False,mode='a')
            print(lat_lon +' is done')
        print(s +' 已完成')
print('ALL DONE')

