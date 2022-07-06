import numpy as np
import matplotlib.pylab as plt
import wave,sys

###Allocation###
raw=wave.open("speech.wav","r")                                 # inputing the speech signal
fs=1000
NTAPS=100
learning_rate=0.001
fnoise=50
new_list=[]
resultant = 0
new_list1 = []
error1=[]


signal=raw.readframes(-1)
signal=np.frombuffer(signal,dtype="int16")

for i in range(len(signal)): 
    new_list.append(signal[i]/32768)

mean = sum(new_list)/len(new_list)                              # mean Calculation

for i in range(len(new_list)):
    resultant = resultant + np.square(new_list[i]-mean)

variance = np.sqrt(resultant/len(new_list))                     # Variance calculation

for i in range(len(new_list)):
    new_list[i] = 0.125 * ((new_list[i]-mean)/variance)

f_rate=raw.getframerate()
time=np.linspace(0,len(new_list)/f_rate,num=len(new_list))


noise = (0.05 * np.random.normal(0,1,len(signal)))              # randomly generated noise signal with range of (-0.2 to + 0.2)


f_rate=raw.getframerate()
time=np.linspace(0,len(new_list)/f_rate,num=len(new_list))

### Created class for Filter session ###

class fir_filter:
    def __init__(self,_coeffecient):
        self.ntaps=len(_coeffecient)
        self.coeffecient=_coeffecient
        self.buffer=np.zeros(self.ntaps)

    def filter(self,v):
        for j in range(self.ntaps-1):
            self.buffer[self.ntaps-j-1]=self.buffer[self.ntaps-j-2]
        self.buffer[0] = v[i]
        return np.inner(self.buffer,self.coeffecient)

    def lms(self,error,mu=0.01):
        for j in range(self.ntaps):
            self.coeffecient[j]=self.coeffecient[j]+error*mu*self.buffer[j]
            error1.append(error)

f=fir_filter(np.zeros(NTAPS))


y=np.empty(len(new_list))

for i in range(len(new_list)):
   #ref_noise=np.sin(2.0*np.pi*fnoise/fs*i)
   #ref_noise=np.random.normal(0,1,len(new_list))
    canceller=f.filter(noise)
    output_signal=new_list[i]-canceller
    f.lms(output_signal,learning_rate)
    y[i]=output_signal

plt.subplot(321)
plt.title("Input Speech Signal")
plt.plot(signal)
plt.grid()

plt.subplot(322)
plt.title("Normalized Signal")
plt.plot(new_list)
plt.grid()

plt.subplot(323)
plt.title("Noise")
plt.plot(noise)
plt.grid()

plt.subplot(324)
plt.title("Normalized Signal + Noise")
plt.plot(new_list + noise)
plt.grid()

plt.subplot(325)
plt.title("Filter Output")
plt.plot(y)
plt.grid()

plt.show()
