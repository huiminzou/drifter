# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:14:24 2018

@author: huimin
"""

import numpy as np
from datetime import datetime,timedelta
import datetime as dt
import matplotlib.pyplot as plt

drifters = np.genfromtxt('drifters_613c_a79f_d040.csv',dtype=None,names=['ids','time','lat','lon','depth','NAN'],delimiter=',',skip_header=1)
try:
    dd=[]
    for aa in np.arange(len(drifters['time'])):
        utc_dt = datetime(int(drifters['time'][aa][0:4]), int(drifters['time'][aa][5:7]), int(drifters['time'][aa][8:10]), int(drifters['time'][aa][11:13]), int(drifters['time'][aa][14:16]), int(drifters['time'][aa][17:19]))#, tzinfo=utc)
        dd.append(utc_dt)
except:
    print 'Time error'
start_time=dt.datetime(2007,6,21,0,0,0)
days=7
end_time=start_time+timedelta(hours=days*24)
########get the index of starttime and endtime###########################
index_start=np.argmin(abs(np.array(dd)-start_time))
index_end=np.argmin(abs(np.array(dd)-end_time))
######plot##########################
FN='necscoast_worldvec.dat'
CL=np.genfromtxt(FN,names=['lon','lat'])
fig,ax=plt.subplots(1,1,figsize=(8,8))
plt.subplots_adjust(wspace=0.1,hspace=0.1)
ax.plot(CL['lon'],CL['lat'],'b-')
for i in range(index_start,index_end+1):
    ax.scatter(drifters['lon'][i],drifters['lat'][i])

ax.scatter(drifters['lon'][index_start],drifters['lat'][index_start],color='green',label='start')
ax.scatter(drifters['lon'][index_end],drifters['lat'][index_end],color='red',label='end')
ax.legend()    
ax.set_xlim([-70.7,-69.9])
ax.set_ylim([41.5,42.1])
ax.set_title('JUN_21-28_2007 surface particle trajectories(Drifter)',fontsize=14)
plt.savefig('particle_tracking_drifter_20070621-28',dpi=200)
plt.show()