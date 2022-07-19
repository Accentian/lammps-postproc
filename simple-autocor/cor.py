from numpy import *
import numpy as N
import pylab as P

fn = 'data.txt'
x = loadtxt(fn,unpack=True,usecols=[1])
time = loadtxt(fn,unpack=True,usecols=[0]) 
ndat = len(time)

def estimated_autocorrelation(x):
    n = len(x)
    variance = x.var()
    x = x-x.mean()
    r = N.correlate(x, x, mode = 'full')[-n:]
    result = r/(variance*(N.arange(n, 0, -1)))
    return result
    
autocor = estimated_autocorrelation(x)
minimum = min(autocor[0:int(ndat/2)])
maximum = max(autocor[0:int(ndat/2)])

P.plot(time,autocor)
P.xlabel('time (s)')
P.ylabel('autocorrelation')
P.xlim([0.0,time[-1]/2])
P.ylim([minimum,maximum])
#P.show()
P.savefig("autocorrelation.png")
