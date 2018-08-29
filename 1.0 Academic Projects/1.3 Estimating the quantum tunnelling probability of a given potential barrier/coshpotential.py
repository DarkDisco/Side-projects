# cosh potential!

from math import cosh, cos, sin, sinh, pi
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

K=1
L=1         # Length of barrier
E=0.8               #  Energy of beam
hbar=1         #1.05457e-34
V0=2            # Regtangualr potential barrier magnitude
m=K*K/(2*E)        #9.11e-31        # mass of an electron
T=1e-9           # fix transmission amplitude           #(2*m*E/hbar**2)*0.5             # set K equal to 1 for simplicity apparently...? 
kappa=(2*m*V0/hbar**2)**0.5      # imaginary wave number?? 

def V(x):
    "Calculates potential"
    V=V0/(cosh(x/L)**2)     # Potential of wavefunction inside the barrier
                
    return V
        
def derivs(n,x,y):
    "DERIVS calculates y' from x and y"
    dy=np.zeros(n+1,float)             # List of n+1 zeros as floats
    dy[1]=y[2]                            # Puts the second order Schrodinger eq into
    dy[2]=(V(x)-E)*y[1]   
    return dy
    
def runkut(n,x,y,h):                 # Does magic... 
    "Advances solution defined by derivs from x to x+h"
    y0=y[:]
    k1=derivs(n,x,y)
    for i in range(1,n+1):
        y[i]=y0[i]+0.5*h*k1[i]
        k2=derivs(n,x+0.5*h,y)
    for i in range(1,n+1):
        y[i]=y0[i]+h*(0.2071067811*k1[i]+0.2928932188*k2[i])
        k3=derivs(n,x+0.5*h,y)
    for i in range(1,n+1):
        y[i]=y0[i]-h*(0.7071067811*k2[i]-1.7071067811*k3[i])
        k4=derivs(n,x+h,y)
    for i in range(1,n+1):
        a=k1[i]+0.5857864376*k2[i]+3.4142135623*k3[i]+k4[i]
        y[i]=y0[i]+0.16666666667*h* a
    x+=h
    return (x,y)

def runkut1(n,x2,y2,h):                 # Does magic... 
    "Advances solution defined by derivs from x to x+h"
    y0=y2[:]
    k1=derivs(n,x2,y2)
    for i in range(1,n+1):
        y2[i]=y0[i]+0.5*h*k1[i]
        k2=derivs(n,x2+0.5*h,y2)
    for i in range(1,n+1):
        y2[i]=y0[i]+h*(0.2071067811*k1[i]+0.2928932188*k2[i])
        k3=derivs(n,x2+0.5*h,y2)
    for i in range(1,n+1):
        y2[i]=y0[i]-h*(0.7071067811*k2[i]-1.7071067811*k3[i])
        k4=derivs(n,x2+h,y2)
    for i in range(1,n+1):
        a=k1[i]+0.5857864376*k2[i]+3.4142135623*k3[i]+k4[i]
        y2[i]=y0[i]+0.16666666667*h* a
    x2+=h
    return (x2,y2)
    
#---------------------------------------- setting inital conditions   
N=80000             #number of steps
x=10.0*pi; y=[0,T,0.0]   # y,y1,y2
x2=10.0*pi ; y2=[0,0.0,T]

#---------------------------------------- plotting wavefunction in space
phi=[0 for j in range(0,N)]          # list for y[1]
phiprime= [0 for j in range(0,N)]    # list of y[2]

chi=[0 for j in range(0,N)]            # second time calling runkut y1
chiprime= [0 for j in range(0,N)]    #y2

xp=[0 for j in range(0,N)]         # list of x values

for j in range(0,N):                       
    (x,y) = runkut(2, x, y, -100.0/N)
    #print x, y[1], y[2]                # prints values for reference
    phi[j]=y[1]            # adds solution y1 the jth index of z
    phiprime[j]=y[2]
    xp[j]=x              # adds x values to list that can be plotted against


for j in range(0,N):
    (x2,y2) = runkut1(2, x2, y2, -100.0/N)
    chi[j]=y2[1]
    chiprime[j]=y2[2]

plt.plot(xp,phi)    # solutions for y1
plt.plot(xp,phiprime)      # solutions for y2 
plt.legend(('phi', 'phiprime'))                 # Plot shows tunnelling throug barrier
plt.xlabel('Distance')
plt.ylabel('Psi displacement')
plt.show()
#plt.plot(V)
#plt.legend(('V'))
#plt.show()

#--------------------------------------- Slicing list to start on LHS of barrier
Nn=int((10*pi +20)*N/100)  # index of the x value list correspoding to 20.559 
phis=phi[-Nn:]          # sliced list to start from ~ -20
phips=phiprime[-Nn:]
chis=chi[-Nn:]
chips=chiprime[-Nn:]
xps=xp[-Nn:]

#------------------------------------Working out incident flux
Iflux=[0 for j in range(0,Nn)]
Rflux=[0 for j in range(0,Nn)]            
Tflux=[0 for j in range(0,Nn)]
Tcoef=[0 for i in range(0,Nn)]

for j in range(0,Nn):   # works out RR* and II*
    Iflux[j]=0.25*((phis[j]+(chips[j]/K))**2 +(chis[j]-(phips[j]/K))**2)
    Rflux[j]=0.25*((phis[j]-(chips[j]/K))**2 +(chis[j]+(phips[j]/K)**2))
    Tflux[j]=Iflux[j]-Rflux[j] 
    Tcoef[j]=(T*T)/Iflux[j]             # 1-(Rflux[j]/Iflux[j])

plt.plot(Tcoef)
plt.show()
print "II*-RR*=", (sum(Iflux)/len(Iflux)) - (sum(Rflux)/len(Rflux))
print "TT*=", T*T
print "Sample from",xp[Nn],"to end."
print "Experimental trans coef. =", sum(Tcoef)/len(Tcoef)

#----------------------------- Theoretical trans coef.
u=kappa*kappa*L*L
if u < 0.25:
    theory=sinh(pi*K*L)**2 / (sinh(pi*K*L)**2 + cos(pi*(0.25-u)**0.5)**2)
else:
    theory=sinh(pi*K*L)**2 / (sinh(pi*K*L)**2 + cosh(pi*(u-0.25)**0.5)**2)
print "Theoretical value =", theory

#---------------------------- Standard Error 

tavg=sum(Tcoef)/len(Tcoef)
for j in range(0,Nn):
    Tcoef[j]=Tcoef[j]-tavg
    Tcoef[j]=Tcoef[j]*Tcoef[j]
sigma=(sum(Tcoef)/(Nn-1))**0.5
print "Sigma =", sigma