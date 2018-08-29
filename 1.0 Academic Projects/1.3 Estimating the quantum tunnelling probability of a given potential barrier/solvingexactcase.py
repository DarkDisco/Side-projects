# Exact case for quanutm tunnelling of rectangle potential

from math import cosh, cos, sinh, pi
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

L=1         # Length of barrier
kappa=1      # imaginary wave number?? 
E=8               #  Energy of beam
hbar=1        #1.05457e-34
V0=10             # Regtangualr potential barrier magnitude
m=2       #9.11e-31        # mass of an electron
T=1           # fix transmission amplitude 
K=1              # set K equal to 1 for simplicity apparently...? 

"""def k(x):                      # Defines k for inside and ouside barrier
    if x>=0 and x<=L:
        k=(2*m*(E-V0)/hbar**2)**0.5
    else: 
        k=((2*m*E)/(hbar**2))**0.5
    return k"""


def V(x):
    "Calculates potential"
    #V=V0/((1+x**2)/2L**2)**2
    V3=0
    if x>=0 and x<=L:           # Potential of wavefunction inside the barrier
        #V=V0/(cosh(x/L)**2)
        return V0
    else:                    # Potential outside barrier
        return V3
        
        
def derivs(n,x,y):
    "DERIVS calculates y' from x and y"
    dy=np.zeros(n+1,float)             # List of n+1 zeros as floats
    #dy=[0 for i in range(0,9+1)]
    dy[1]=y[2]                            # Puts the second order Schrodinger eq into
    dy[2]=(V(x)-E)*y[1]  #*(2*m/hbar**2)   
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
    

#--------- setting inital conditions   
xmax=400             #number of steps
x=5; y=[0,T,0.0]   # y,y1,y2


#------- plotting 
z=[0 for j in range(0,xmax)]          # list of zeros for a variable y[1]
r=[0 for j in range(0,xmax)]            # list of y[2]
xp=[0 for j in range(0,xmax)]         # list of x values
zeroline = [0 for j in range(0,xmax)]  # creates line at y=0
phi= [0 for j in range(0,xmax)]      # values of phi 
phiprime= [0 for j in range(0,xmax)]      # values of phi'
chi= [0 for j in range(0,xmax)]         # values of chi
chiprime= [0 for j in range(0,xmax)]        #values of chi'

for j in range(0,xmax):                       
    (x,y) = runkut(2, x, y, -10.0/xmax)
    #print x, y[1], y[2]                # prints values for refference
    z[j]=y[1]            # adds solution y1 the jth index of z
    r[j]=y[2]
    xp[j]=x              # adds x values to list that can be plotted against
    phi[j]=T*cos(K*x)             # Adds phi at certain x value to open list
    chi[j]=T*sin(K*x)
    phiprime[j]=-T*K*sin(K*x)
    chiprime[j]=T*K*cos(K*x)
    

#py.plot(zeroline)
#plt.plot(xp,z)    # solutions for y1
plt.plot(xp,r)      # solutions for y2 
#plt.legend(('Phi', 'Phi Prime'))
plt.xlabel('x [au]')
plt.ylabel('Psi(x) [au]')
someX, someY = 0, 0                  # Adds rectangle for barrier
currentAxis = plt.gca()
currentAxis.add_patch(Rectangle((someX - 0.0, someY - 20), 1, 40,
                      alpha=1, facecolor='r'))

plt.savefig("example of wavefunction2.pdf", bbox_inches="tight")

#------------  working out transmission coeffienct

# TT*=II* -RR*
Tflux= [0 for j in range(0,xmax)]          # open list for TT*
Tcoefficent= [0 for i in range(0,xmax)]  # T coeffiecent values
Iflux= [0 for i in range(0,xmax)]          # II*
Rflux= [0 for i in range(0,xmax)]      # RR*
Rcoefficent= [0 for i in range(0,xmax)]
t2= [0 for i in range(0,xmax)]


for j in range(0,xmax):   # works out T for corresponding x value
    Iflux[j]=0.25*((phi[j]+(chiprime[j]/K))**2 +(chi[j]-(phiprime[j]/K))**2)
    Rflux[j]=0.25*((phi[j]-(chiprime[j]/K))**2 +(chi[j]+(phiprime[j]/K)**2))
    Tflux[j]=Iflux[j]-Rflux[j]
    Tcoefficent[j]=1-(Rflux[j]/Iflux[j])        # 1=RR*/II*
    t2[j]=Tflux[j]/Iflux[j]                   # TT*/II*

#------------------- Plotting transmission coefficent 

#plt.plot(Tflux)
"""plt.plot(Tcoefficent)
plt.legend('Transmission coef.')
plt.show()"""


"""plt.plot(Rcoefficent)
plt.legend('Refletion coefficent')
plt.show()"""

Iflux1=[0 for i in range(0,200)]         #cuts the solution list to region 
Rflux1= [0 for i in range(0,200)]        # before the barrier
plotv= [0 for i in range(0,200)]
xp1= [0 for i in range(0,200)]
for j in range(0,200):
    n=200
    Iflux1[j]=Iflux[j+n]
    Rflux1[j]=Rflux[j+n]
    xp1[j]=xp[j+n]
    n+=1
    
for i in range(0,200):
    plotv[i]= 1-(Rflux1[i]/Iflux1[i])
#plt.plot(xp1,plotv)
avg=sum(Tcoefficent)/len(Tcoefficent)
print avg


#------------- Calculating theoretical transmission coefficent
"""if kappa*kappa*L**2 < 0.25:
    Ttheory=sinh(pi*K*L)**2 / (sinh(pi*K*L)**2 +cosh(pi(0.25-kappa*kappa*L*L)**0.5))
else:
    Ttheory=sinh(pi*K*L)**2 / (sinh(pi*K*L)**2 +cosh(pi(kappa*kappa*L*L-0.25)**0.5))

print Ttheory"""

y=[1,2,3,4,5,6]
for i in range(0,3):
    y.pop(0)
    
print y



