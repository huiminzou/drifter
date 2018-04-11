# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:39:27 2018

@author: huimin
"""

import numpy as np
from datetime import datetime,timedelta
import datetime as dt
import matplotlib.pyplot as plt
###############drifter###############################
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
for i in range(index_start,index_end):
    ax.plot([drifters['lon'][i],drifters['lon'][i+1]],[drifters['lat'][i],drifters['lat'][i+1]],color='red')
ax.plot([drifters['lon'][i],drifters['lon'][i+1]],[drifters['lat'][i],drifters['lat'][i+1]],color='red',label='drifter')
ax.text(drifters['lon'][index_start]+0.01,drifters['lat'][index_start]-0.02,'start',fontsize=12)
ax.text(drifters['lon'][index_end]+0.02,drifters['lat'][index_end],'end')
##############FVCOM#############
m26=np.load('/home/hxu/huiminzou/from xiaojian/particle-tracking-using-fvcom-model-master/30yr_FVCOM2007621_7days_1point.npy')#'m_ps2011-2010_630.npy'
p=m26.tolist()

for a in np.arange(len(p['lon'][0])):
    if len(p['lon'][0][a])>=361: 
        print 'ooooooooooooooooooooooooooooooooooooooooooooooooooo '
        ax.scatter(p['lon'][0][a][360],p['lat'][0][a][360],color='red')
        ax.text(p['lon'][0][a][360],p['lat'][0][a][360],'end',fontsize=12)
        ax.plot([p['lon'][0][a][0],p['lon'][0][a][360]],[p['lat'][0][a][0],p['lat'][0][a][360]],'g-')#,linewidth=0.5)
    else:
        ax.scatter(p['lon'][0][a][-1],p['lat'][0][a][-1],color='red')
        ax.text(p['lon'][0][a][-1],p['lat'][0][a][-1],'end',fontsize=12)
        ax.plot(p['lon'][0][a][0:],p['lat'][0][a][0:],'g-',label='GOM3')#,linewidth=0.5)

###################ROMS###############################
data_file=np.load('/home/hxu/huiminzou/from xiaojian/particle-tracking-using-roms-model-master/particle-tracking-using-roms-model-master/20180411/ROMS_2007-6-21_28_1point.npy')
data=data_file.tolist()
ax.scatter(data['lon'][0][0],data['lat'][0][0],color='green')
ax.scatter(data['lon'][0][-1],data['lat'][0][-1],color='red')
ax.text(data['lon'][0][-1],data['lat'][0][-1],'end',fontsize=12)
ax.plot(data['lon'][0][0:],data['lat'][0][0:],'y-',label='ROMS')#,linewidth=0.5)
ax.legend()    
ax.set_xlim([-70.7,-69.9])
ax.set_ylim([41.5,42.1])
ax.set_title('JUN_21-28_2007 surface particle trajectories',fontsize=14)
plt.savefig('particle_tracking_drifter_20070621-28',dpi=200)
plt.show()