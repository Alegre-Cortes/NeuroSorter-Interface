# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:20:42 2021

@author: jalegre
"""

#%%
from decorators.time_consuming import timeit 

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

@timeit
def run(spike_dict, current):

    cmapname = 'Set1'
    cmap = plt.get_cmap(cmapname)
    
    channelMap = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                           17,18,19,20,21,22,23,24,25,16,17,18,19,30,31,32])
    
    electrodeMap = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                           17,18,19,20,21,22,23,24,25,16,17,18,19,30,31,32])
    
    plot_arr = np.arange(32).reshape((16, 2)) / 31.
    
    experiments = np.unique(spike_dict['ExperimentID'])

    for experiment in experiments:

        fig = plt.figure()
        for channel in range(1,32):
            index = [it for it, channelID in enumerate(spike_dict['ChannelID']) if channelID == channel and spike_dict['ExperimentID'][it] == experiment and spike_dict['UnitID'][it] > -1]
            waveforms = [spike_dict['Waveforms'][idx] for idx in index]
            units = [spike_dict['UnitID'][idx] for idx in index]

            idx = [idx for idx,ch in enumerate(channelMap) if ch == channel][0]
        
            plt.subplot(16, 2, idx+1)
            for wave,unit in zip(waveforms,units):
                plt.plot(wave, color=cmap(plot_arr[unit%16, unit%2])) 
            
            plt.axis('off')
            plt.title('E'+str(electrodeMap[idx])+'CH'+str(channelMap[idx]))
        fig.tight_layout()
        plt.show()


        