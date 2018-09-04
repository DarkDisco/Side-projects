import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import linregress

s=[-1,1] # Used to define movement in positive or negative direction

def drunkardswalk(nsteps, nwalks=1000, wellwidth=20):
    """Input= max steps for 1 walker; number of walkers; well width/2 """
    
    
    for x in range(0,nwalks):      # Iterates nwalks times to increase resolution
        j=0   #Starting position origin
        
        for i in range(0,nsteps):   # Iterates code from 0 to max step no.
            j+=random.choice(s)       # Generates random +/- sign for direction of step
            
            if abs(j)==wellwidth:    # Codition for arrest 
                nwalks-=1      #confirms one arrest
                break
            
    return nwalks

 
# Plotting
# Ideal value -0.019
# closest exp value -0.0193 
 
x = range(60,200)
k = [drunkardswalk(i,100000) for i in x]  
    
plt.plot(x,np.log(k), ".b")
plt.grid()
plt.title("Plot of the Rate of Termination for a One-Dimensional Well  ")
plt.xlabel("Number of steps")
plt.ylabel("log(k)")
#plt.legend("Ground state termination rate",)
print linregress(x,np.log(k))

            
