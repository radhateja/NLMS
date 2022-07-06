
import numpy as np
import matplotlib.pyplot as plt
import nlms as nlms
from misc import mswe
# Get u(n) - this is available on github or pypi in the examples folder
u = np.load('speech.npy')
plt.subplot(161)
plt.plot(u) 
plt.title( "input signal,u(n)")
plt.grid()
# Generate received signal d(n) using randomly chosen coefficients
coeffs = np.concatenate(([0.8], np.zeros(8), [-0.7], np.zeros(9),
                         [0.5], np.zeros(11), [-0.3], np.zeros(3),
                         [0.1], np.zeros(20), [-0.05]))
w = np.array(coeffs)
d = np.convolve(u, coeffs) #echos is added in the input signal
plt.subplot(162)
plt.plot(d)
plt.grid()
# Add background noise
v = np.random.randn(len(d)) * np.sqrt(5000)
d += v

# Apply adaptive filter
M = 100  # Number of filter taps in adaptive filter
step = 0.1  # Step size
y, e, w = nlms.nlms(u, d, M, step)

# Calculate mean square weight error
#mswe = mswe(w, coeffs)

# Plot speech signals
plt.subplot(163)
plt.title("Speech signals")
plt.plot(u, label="input speech signal, u(n)")
plt.plot(d, label="echo Speech signal , d(n)")
plt.grid()
plt.legend()
plt.xlabel('Samples')

plt.subplot(164)
plt.plot(y)
plt.title("output signal")
plt.grid()
plt.subplot(165)
plt.plot(w)
plt.title("filter coefficients")
plt.grid()
# Plot error signal - note how the measurement noise affects the error
plt.subplot(166)
plt.title('Error signal e(n)')
plt.plot(e)
plt.grid()
plt.xlabel('Samples')
"""
# Plot mean squared weight error - note that the measurement noise causes the
# error the increase at some points when Emily isn't speaking
plt.figure()
plt.title('Mean squared weight error')
plt.plot(mswe)
plt.grid()
plt.xlabel('Samples')

# Plot final coefficients versus real coefficients
plt.figure()
plt.title('Real coefficients vs. estimated coefficients')
plt.plot(w[-1], 'g', label='Estimated coefficients')
plt.plot(coeffs, 'b--', label='Real coefficients')
plt.grid()
plt.legend()
plt.xlabel('Samples')
"""
plt.show()
