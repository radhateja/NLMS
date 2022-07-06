import numpy as np
import matplotlib.pylab as plt
import wave,sys
#from nlms import nlms

raw=wave.open("male.wav","r")
fs=1000
NTAPS=100
learning_rate=0.001
fnoise=50



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



signal=raw.readframes(-1)
signal=np.frombuffer(signal,dtype="int16")
f_rate=raw.getframerate()
time=np.linspace(0,len(signal)/f_rate,num=len(signal))
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

y=np.empty(len(signal))
for i in range(len(signal)):
    ref_noise=np.sin(2.0*np.pi*fnoise/fs*i)
    #ref_noise=np.random.normal(0,1,len(signal))
    canceller=f.filter(ref_noise)
    output_signal=signal[i]-canceller
    f.lms(output_signal,learning_rate)
    y[i]=output_signal

"""y,e,w = nlms()"""
plt.figure(2)
plt.plot(y)
plt.show()
