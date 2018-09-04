# Circular well 2D 
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import linregress



def circular_qrw(nsteps, nwalks=1000, wellradius=15):
    
    """"Input = No. Steps, No. walkers/trials, Well radius
            , Energy level(0,1,2)"""

    up= np.array([0,1])          # Defines a movement upwards
    right= np.array([1,0])
    down= np.array([0,-1])
    left= np.array([-1,0])
    amove= [up, down, left, right] # lists possible movements
    
    b=0.6    # 
    #lowwerbound=  ((1/3)*wellradius)-b  # Not used
    #upperbound= ((1/3)*wellradius)+b
    
    for i in range(0,nwalks): # Iterate the for loop over range provided
        
        position=np.array([-7,-5])  # Starting position 
        
        for p in range(0,nsteps): 
            
            position+= random.choice(amove)   # current position is equal to the old position + random allowed move
            R= ((abs(position[0]))**2 + (abs(position[1]))**2)**0.5         # Boundary of circular well      
            
            if R >= wellradius: # if position of walker is greater than the radius of the well, reduce number of walkers by 1
                nwalks=nwalks -1
                break  # s
            #if lowwerbound<= R <= upperbound:
             #   nwalks=nwalks -1
              #  break
    
    return nwalks
    
    
    
#plotting

x = np.arange(25,85)  # A step count below 25 doesn't give walkers a chance to reach the boundary (contain no information about energy level) 
# k defines the number of walks that have survived n steps.
k = np.array([circular_qrw(i,100000) for i in x])  # Populates array with values from the function circular_qrw, over defined x range
    
plt.plot(x,np.log(k), ".b") # ".b" forces graph to be plotted using blue points instead of a line.
plt.grid()
#plt.title("Rate of Termination for a Two-Dimensional Well Ground state ")
plt.xlabel("Number of steps")
plt.ylabel("log(k)")
plt.show()
print linregress(x,np.log(k))     # Used for error analysis
            
        
