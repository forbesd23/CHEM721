# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 16:36:05 2024
@author: forbe
"""
import numpy as np
import matplotlib.pyplot as plt
#%%
f = 1500 #1.5 kHz
t = np.linspace(0,.0030,1000) #time
w = 2*np.pi*f
Vpp = .1 #Voltage peak to peak
#Vin = Vpp * np.sin(w*t) #VIn fucntion
Vin = Vpp * np.exp(w*t*1j)
#%%
def invertOpAmp(R1,R2,Vin): #Solve inverting Op Amp
    Vout = -Vin*(R2/R1)
    return Vout
def noninvertOpAmp(R1,R2,Vin): #solve non inverting Op Amp
    Vout = Vin*(1+R1/R2)
    return Vout
def PlotOpAmp(t,Vin,Vout,Q): #ploting Vin and Vout
    plt.plot(t,Vin, label = 'Vin')
    plt.plot(t,Vout, label = 'Vout')
    plt.xlabel('time')
    plt.ylabel('Voltage')
    plt.ylim(-1.5,1.5)
    plt.title('Op-Amp Circuit Question ' + Q)
    plt.legend()
    return plt
#%%
I = True #define inverting op amp as true
N = False #define non inverting op amp as fasle
RC = 10000 + (-1j)/(w*10*(10**(-9))) # solve q5 R2 value
#%%
QN = [0,1,2,3,4] #question number
OpAmpIN = [N,I,N,I,I] #selecting op amp type for each Q
R1t = [.00000001,1000,10000,10000,1000] #selecting R1 for each Q
R2t = [.0000001,10000,1000,10000,RC] #selectig R2 for each Q
#%%
for Q in QN: #Chose method to solve each question and plot each question
    if OpAmpIN[Q] == True:
        Vout = invertOpAmp(R1t[Q], R2t[Q], Vin)
    if OpAmpIN[Q] == False:
        Vout = noninvertOpAmp(R1t[Q], R2t[Q], Vin)
    Q = str(Q+1)
    OpAmp = PlotOpAmp(t, Vin, Vout, Q)
    plt.show()