# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:40:51 2021

@author: jalegre
"""

#%%
from decorators.time_consuming import timeit 

from seaborn import distplot
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')


@timeit
def run(spike_dict, current):


    index = current['plotted']
    time_stamps = np.empty((1,len(index)))
    wave_forms = np.empty((48,len(index)))
    units = np.empty((1,len(index)))
    for j in range(0,len(index)):
        time_stamps[0,j] = (spike_dict["TimeStamps"][index[j]])/20 #TimeStamp of each spike is obtained 
        wave_forms[:,j] = (spike_dict["Waveforms"][index[j]]) #Waveform of each spike is obtained
        units[0,j] = spike_dict["UnitID"][index[j]]
        
    # Plotting
    colours = plt.get_cmap('Set1')    
    #Create a variable with the colours of interest
    plt.figure() #Create a figure
    plt.xlabel('Time (ms)')
    plt.ylabel('uV')
    for j in np.unique(units):
        trans = np.where(units==j) 
        #Select the spikes in each unit
        trans = trans[1]        
        color = colours(int(j))
        distplot(trans, hist=False,  rug=True,
             axlabel="Something ?",
             kde_kws=dict(label="kde"),
             rug_kws=dict(height=.2, linewidth=2, color=color))

