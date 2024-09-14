# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:46:12 2024

@author: forbe
"""

import numpy as np
import matplotlib.pyplot as plt
#%%
def BodeVoltageGainVgain(Vratio):
    Vgain = 20*np.log10(Vratio)
    return Vgain
def RCLowPass(w,R,C):
    VLowPass = abs(1/np.sqrt(1+(w*R*C)**2))
    return VLowPass
def RCHighPass(w,R,C):
    VHighPass = abs(w*R*C/np.sqrt(1+(w*R*C)**2))
    return VHighPass
def BodePlot(Vgain,f,labels):
    plt.plot(f,Vgain, label= labels)
    plt.ylabel('Vout / Vin')
    plt.xlabel('Log(frequency)')
    plt.xlim(0,100000)
    plt.xscale('log',base =10)
    plt.legend()
    return plt

f = np.logspace(1,6,num=600,base=10)
w = 2*np.pi*f
#%%
R = [47*10**3,1*10**3]
C = [0.2*10**-6, 0.1*10**-6]
index = [0,1]

for i in index:
    VLow = RCLowPass(w, R[i], C[i])
    VHigh = RCHighPass(w, R[i], C[i])
    VRatio_Low = BodeVoltageGainVgain(VLow)
    VRatio_High = BodeVoltageGainVgain(VHigh)
    i = str(i +1)
    V_plot_Low = BodePlot(VRatio_Low, f,'Low Pass '+ i)
    V_plot_High = BodePlot(VRatio_High, f,'High Pass '+ i)

    plt.show()

