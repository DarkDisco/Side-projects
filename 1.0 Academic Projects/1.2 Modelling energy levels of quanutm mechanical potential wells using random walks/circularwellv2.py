# Circular well 2D 
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import linregress



def circular_qrw(nsteps, nwalks=1000, wellradius=15):
    
    """"Input = No. Steps, No. walkers/trials, Well radius
            , Energy level(0,1,2)"""

    up= np.array([0,1])
    right= np.array([1,0])
    down= np.array([0,-1])
    left= np.array([-1,0])
    amove= [up, down, left, right]
    
    b=0.6    
    lowwerbound=  ((1/3)*wellradius)-b  
    upperbound= ((1/3)*wellradius)+b
    
    for i in range(0,nwalks):
        
        position=np.array([-7,-5])  # Starting position 
        
        for p in range(0,nsteps):
            
            position+= random.choice(amove)   
            R= ((abs(position[0]))**2 + (abs(position[1]))**2)**0.5         # Boundary of circular well      
            
            if R >= wellradius:
                nwalks=nwalks -1
                break
            #if lowwerbound<= R <= upperbound:
             #   nwalks=nwalks -1
              #  break
           """if position[0]>= 0:
                nwalks=nwalks-1
                break
            if position[1]>=0:
                nwalks=nwalks-1
                break"""
    
    return nwalks
    
    
    
#plotting

x = np.arange(25,85)
k = np.array([circular_qrw(i,100000) for i in x])  
    
plt.plot(x,np.log(k), ".b")
plt.grid()
#plt.title("Rate of Termination for a Two-Dimensional Well Ground state ")
plt.xlabel("Number of steps")
plt.ylabel("log(k)")
plt.show()
print linregress(x,np.log(k))
            
        