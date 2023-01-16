import numpy as np
import matplotlib.pyplot as plt
rho0 = 1.205 
c = 343 
f = np.linspace(377,3400,30)
k = 2*np.pi*f[:]/c 
L = 33/100
x1= 10/100
s = 3.75/100 
p1 = np.loadtxt(r"", usecols=[1,2])
p2 = np.loadtxt(r"", usecols=[1,2])
p1=p1[:,0]+p1[:,1]*1j  
p2=p2[:,0]+p2[:,1]*1j   
H12 = p2/p1       
Hh = np.exp(-1j*k*s)  
Hr = np.exp(1j*k*s)   
r = np.abs(((H12-Hh)/(Hr-H12)) * np.exp(1j*2*k*(x1)))
alpha = 1-r**2
plt.rcParams["figure.figsize"] = (20,8)
fig = plt.figure()
ax = plt.axes()
plt.xlim([377, 3400])
plt.ylim([0, 1])
plt.ylabel("Absorption Coefficient")
plt.xlabel("Frequrency (Hz)")
ax.plot(f, alpha);
plt.savefig('SimResults.png')