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
    plt.plot(np.log10(f),Vgain, label= labels)
    plt.ylabel('20*log(Vout / Vin)')
    plt.xlabel('log(frequency)')
    plt.xlim(-2,6)
    plt.ylim(-30,5)
    plt.legend()
    return plt
def BodePhaseHigh(w,R,C, labels):
    PhaseS = np.degrees(np.arctan(1/(w*R*C)))
    plt.plot(np.log10(f),PhaseS, label= labels)
    plt.ylabel('Phase Shift')
    plt.xlabel('log(frequency)')
    plt.legend()
    return plt
def BodePhaseLow(w,R,C, labels):
    PhaseS = np.degrees(-np.arctan((w*R*C)))
    plt.plot(np.log10(f),PhaseS, label= labels)
    plt.ylabel('Phase Shift (degrees)')
    plt.xlabel('log(frequency')
    plt.ylim(-100,100)
    plt.legend()
    return plt
def VOutPlot(Vgain,t,labels):
    V_step = Vgain * Vbool
    plt.plot(t,V_step)
    plt.title(labels)
    plt.xlabel('time (s)')
    plt.ylabel('Voltage Output')
    plt.xlim(0,1)
    return plt

f = np.logspace(-2,6,num=1000,base=10)
w = 2*np.pi*f
t = 1/f

Vbool = (t>.1)
plt.plot(t,Vbool)
plt.xlim(0,1)
plt.show()
#%%
R = [47*10**3,1*10**3]
C = [0.2*10**-6, 0.1*10**-6]
index = [0,1]

for i in index:
    VLow = RCLowPass(w, R[i], C[i])
    VHigh = RCHighPass(w, R[i], C[i])
    VRatio_Low = BodeVoltageGainVgain(VLow)
    VRatio_High = BodeVoltageGainVgain(VHigh)
    j = str(i +1)
    V_plot_Low = BodePlot(VRatio_Low, f,'Low Pass '+ j)
    V_plot_High = BodePlot(VRatio_High, f,'High Pass '+ j)
    plt.title('Frequency vs 20*log(Vgain)')
    plt.show()
#%%
for i in index:
    PhaseLow = BodePhaseLow(w, R[i], C[i], 'Low ' + str(i +1))
    PhaseHigh = BodePhaseHigh(w, R[i], C[i], 'High ' + str(i +1))
    plt.title('Frequency vs Phase Shift')
    plt.show()
#%%

#%%
for i in index:  
    j = str(i +1)
    VLow = RCLowPass(w, R[i], C[i])
    VOut = VOutPlot(VLow, t,'Low Pass '+ j)
    plt.show()
    VHigh = RCHighPass(w, R[i], C[i])
    VOut = VOutPlot(VHigh, t,'High Pass '+ j)
    plt.show()
