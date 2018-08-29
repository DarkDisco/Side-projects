#Algorithm for finding Lamda with small errors

import numpy as np
import pylab as py
from random import choice 


k=np.zeros(101,int) # no. of dunkards that reached a certain distance index=no. steps
jv=[-1,1]   # Allows for randon selection of +,-
d=[] # Distance 0-100
e=[]
n=100  #no. steps drunkard is allowed to take
nwalks=1000   # no. times a drunkards walk is performed

def drunkardswalk(n):
    "Computes distance moved after n random steps."
    j=0 # Walk starts at origin
    h=0 # Count for a single dunkard
    jmax=100  # Max no. of steps allowed
    for i in range(0,jmax,1):    # Condition to stop interating at 100 steps
        j+=(choice(jv)) # j=j+1  or j=j-1
        h+=1            # No. of steps taken before an arrest
        if abs(j)==8 or h==100:    # Condition to limit no. steps in same direction to 8
            break      # Ends loop
    d.append(h)    # Condition to find distance travelled before arrest
     
    """for i in range(0,jmax,1):    # Required to get negative step count
        j+=(choice(jv)) # j=j+1  or j=j-1
                    
        if abs(j)==8 or h==100:    
            break       
        h+=1
    e.append(h)"""
    return d, j, h  # Returns no. steps 

 
for i in range(0, nwalks): #for loop iterates drunkardswalk function nwalks times
    drunkardswalk(n)

#w=sorted(map(abs,d)) # List w sorts the values of list d into assending order



for x in range(0,len(d),1): # For loop adds +1 to an index of k for each value of d
    k[d[x]]=k[d[x]]+1  # even steps
    #k[e[x]]=k[e[x]]+1  # odd steps
    
    

kv=[] # open list for 8-100 values
for i in range(8,101,1):  # chops list downn to aviod first 7 values 
    kv.append(k[i])



print kv
py.plot(range(8,101,1),np.log(kv),'.r',)
py.show()
print np.gradient(range(8,101,1),np.log(kv))

"""a=[]      # To take averages of 5 iterations of the program...
b=[]
c=[]
d=[]
e=[]
finalavgK=[]  
biglist=[a,b,c,d,e]
for i in range(0,5,1):
    #iterate nwalks and drunkardswalk
    i+=1
    biglist[i].append(k)
    

for i in len(k):
    ((a[i]*b[i]*c[i]*d[i]*e[i])/5) =temp[i]
    finalavgK.append(temp[i])"""
    
    
    
      