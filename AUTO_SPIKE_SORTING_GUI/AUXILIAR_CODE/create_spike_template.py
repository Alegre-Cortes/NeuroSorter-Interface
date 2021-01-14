# -*- coding: utf-8 -*-
"""
@author: %(Mikel Val Calvo)s
@email: %(mikel1982mail@gmail.com)
@institution: %(Dpto. de Inteligencia Artificial, Universidad Nacional de Educación a Distancia (UNED))
@DOI: 
"""

import numpy as np 
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import matplotlib
matplotlib.use('Qt5Agg')

def run(spike_dict, current):

    waveforms = []
    
    plt.figure()    
    for index in current['plotted']:
        plt.plot(spike_dict['Waveforms'][index], 'c')
        waveforms.append(spike_dict['Waveforms'][index])
    plt.plot( np.array(waveforms).mean(axis=0) , 'm')
    plt.show()
    mypath = './CLEANER/spike_templates/'
    numfiles = len([f for f in listdir(mypath) if isfile(join(mypath, f))])

    np.save(  './CLEANER/spike_templates/spike_template_' + str(numfiles) + '.npy', np.array(waveforms).mean(axis=0))
    
        
        
       