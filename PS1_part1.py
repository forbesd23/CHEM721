# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:06:21 2024

@author: forbe
"""

import numpy as np
import matplotlib.pyplot as plt
#%% Defining V=IR var

def ResistanceSum(R1,CdS_R):
    Rt_return = R1 + CdS_R
    return Rt_return

def CdSVoltageOutput(V_s,CdS_R,Rt):
    CdS_V_return = V_s * (CdS_R/Rt)
    return CdS_V_return
#%%
V_s = 5
R1 = 10000
I_R1 = V_s / R1
Light_Intensity = np.linspace(1,100,num=1000)
CdS_R = 100000/(Light_Intensity)

#%%
Rt_1 = ResistanceSum(R1,CdS_R)
CdS_V_1 = CdSVoltageOutput(V_s, CdS_R, Rt_1)

#%% linear plot of R vs LI

plt.plot(Light_Intensity, CdS_R/1000)
plt.title('Resistance vs Light Intensity')
plt.xlabel('Relative Light Intesnity')
plt.ylabel('Cds Resistance (k ohms)')
plt.show()


#%%
plt.plot(Light_Intensity,CdS_V_1, 'b', label = '10 kohm Resistor')
plt.title('CdS Voltage Output vs Light Intensity')
plt.xlabel('Relative Light Intesnity')
plt.ylabel('CdS Voltage output (V)')
#plt.show()

#%% Change R to 10 kohms
R2 = 1000
Rt_2 = ResistanceSum(R2,CdS_R)
CdS_V_2 = CdSVoltageOutput(V_s, CdS_R, Rt_2)

#%% plot higher R1 value for Cds voltage
plt.plot(Light_Intensity,CdS_V_2, 'r', label = '1 kohm Resistor')
plt.title('CdS Voltage Output vs Light Intensity')
plt.xlabel('Relative Light Intesnity')
plt.ylabel('CdS Voltage output (V)')
plt.legend()
plt.show()

