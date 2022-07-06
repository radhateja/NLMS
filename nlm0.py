import numpy as np
import matplotlib.pylab as plt
import random
import wave,sys
import math
import nlms
from pydub.playback import play
from pydub.playback import *
#from pydub.playback import Audiosegment

raw=wave.open("male.wav","r")
signal=raw.readframes(-1)
signal=np.frombuffer(signal,dtype="int16")
#print(signal)
print("length=",len(signal))

signal1=[]

for i in range(0,len(signal)):
    signal1.append(signal[i]//32768)
#print(signal1)
mean=sum(signal1)/len(signal1)          # mean value 
print("mean=",mean)

s=0

for i in range(0,len(signal1)):
    s+=(signal1[i]-mean)**2
s=s/len(signal)
s=math.sqrt(s)                          # Deviation

print("deviation=",s)
print("max=",max(signal1))
print("min=",min(signal1))

f_rate=raw.getframerate()
time=np.linspace(0,len(signal)/f_rate,num=len(signal))
y=[]                                    # y is initialised with an empty array
for i in range(0,len(signal1)):
    y.append(0.2*(signal1[i]-mean)/s)
noise=np.random.normal(0,1,len(signal)) # Randomly generated noise based on length of input signal
x=np.fft.fft(y)
p = signal1 + noise

#print(x)
#seg.export(p,"wav")
#t, e, w = nlms.nlms(signal, p, 20 ,1) 
#wav_file = 0 
# Export louder audio file 
#wav_file.export(out_f = "p", format = "wav")

'''
class fir_filter:
    def __init__(self,_coeffecient):
        self.ntaps=len(_coeffecient)
        self.coeffecient=_coeffecient
        self.buffer=np.zeros(self.ntaps)

    def filter(self,v):
        for j in range(self.ntaps-1):
            self.buffer[self.ntaps-j-1]=self.buffer[self.ntaps-j-2]
        self.buffer[0]=v
        return np.inner(self.buffer,self.coeffecient)

    def lms(self,error,mu=0.01):
        for j in range(self.ntaps):
            self.coeffecient[j]=self.coeffecient[j]+error*mu*self.buffer[j]

f=fir_filter(np.zeros(NTAPS))
'''
#p = Audiosegment.from_file("raw") + Audiosegment.from_file("noise")
#play(p)

print()
print("e::",e)
print()
print("w::",w)
plt.figure(1)
plt.title("sound wave")
plt.xlabel("time")
plt.subplot(2,2,1)
plt.title("input signal")
plt.plot(time,signal,'r')
plt.subplot(2,2,1)
plt.title("y[n]")
plt.plot(time,y)
plt.subplot(2,2,2)
plt.title("noise")
plt.plot(time,noise)
plt.subplot(2,2,3)
plt.title("error")
plt.plot(e)
plt.subplot(2,2,4)
plt.title("output signal")
plt.plot(t)
plt.show()
