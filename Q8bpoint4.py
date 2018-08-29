##Monte Carlo Simulation- Model for thre dimensional uranium##

from numpy import random 
from math import pi , cos , acos , sin
from neutrons import neutrons, diffusion

       
a=1.7 #mean free path between the neutron hitting another nucleus and bouncing off units cm
b=21#mean free path between neutron hitting a nucleus and causing fission
R=(2*a*b)**(0.5)#RMS distance a neutron moves before causing fission
T=[]
w=[]
l=16.23019

for v in range(0,10,1):
    
    for i in range (0,100000):#number of inital collisions 
        x=l*random.random()#random position for initial fission in x-axis
        y=l*random.random()#inital position y axis
        z=l*random.random()#inital position z axis
    
        for i in range(0,neutrons()):#function generates average of 2.5 neutrons
            theta=acos(2.0*random.random()-1.0)#defines polar coordinate theta
            phi=2.0*pi*random.random()
            s=R*diffusion()
    
            x2=x+s*sin(theta)*cos(phi)#coordinates for secondary fission x,y,z 
            y2=y+s*sin(theta)*sin(theta)
            z2=z+s*cos(theta)
            
            if 0<=x2<=l and 0<=y2<=l and 0<=z2<=l:
                T.append(1)#count if all co-ordinates are between 0 and L 
                
                
            
        
    if (len(T)/100000.0)>=1:
        w.append(1)

if len(w)==10:       
    print 'critical length is' ,l
else:
    print 'L value either to small or in 100 iterations had a ratio less than 1.'
                     
   




                                                
