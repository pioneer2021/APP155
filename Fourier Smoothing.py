from numpy import zeros, sin, linspace, cos, tan, loadtxt
import numpy as np
from pylab import plot,show, xlabel, ylabel, xlim, ylim
from cmath import exp,pi

def dft(y):
    N = 100
    c = zeros(N,complex)
    for k in range(N):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c
    print(c)

#i = loadtxt("dow.txt",float)
j = linspace(0,10,100)
i = sin(j) + np.random.random(100) - 0.5
c = dft(i)
#C = np.fft.fftshift(c)
print("")
print("The noisy function...")
plot(i)
show()
print(c)
plot(abs(c))
xlabel("frequency")
ylabel("amplitude")
print("")
print("Fourier transform of this...")
show()

## Smoothening process...

print("")
print("After smoothening....")
def dft(y):
    N = 100
    d = zeros(N,complex)
    for k in range(N):
        for n in range(N):
            d[k] += y[n]*exp(-2j*pi*k*n/N)
        for k in range (5,96):          #This will smothen from freq 5 to 95
            for n in range(5,96):    #This will smothen from freq 5 to 95
                d[k] = 0
#        for n in range (60,100):
#            d[k] = 0
    return d
    
    
j = linspace(0,10,100)
i = sin(j) + np.random.random(100) - 0.5
d = dft(i)
#D = np.fft.fftshift(d)
print(d)
plot(abs(d))
xlabel("frequency")
ylabel("amplitude")
xlim(-10,110)
show()

## Inverse Fourier Transform
print("")
print("Inverse Fourier Transform...")
print("The orange plot is the noisy original function.")

FTinvd = np.fft.ifft(d)
plot(FTinvd)
xlabel("frequency")
ylabel("amplitude")
plot(i)
show()