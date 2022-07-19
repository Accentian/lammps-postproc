import numpy as np

x = np.linspace(0,100,num=100000)
y = np.sin(x)

x = np.array([x]).T
y = np.array([y]).T

dat = np.concatenate((x,y),axis=1)
np.savetxt("data.txt",dat)
