##Monte Carlo Simulation- Model for one dimensional uranium ##

from numpy import random,zeros

l=10# length of uranimum x-axis units cm 

a=1.7 #mean free path between the neutron hitting another nucleus and bouncing off units cm
b=21#mean free path between neutron hitting a nucleus and causing fission
R=(2*a*b)**(0.5)#RMS distance a neutron moves before causing fission

mr=zeros(1,float)#bin for secondary neutrons moving right
ml=zeros(1,float)#bin for secondary neutrons moving left
sf=zeros(1,float)#bin for number of secondary fission events


for i in range(0,100):#perform iteration 100 times
    ff=l*random.random()#produces value for position ofintial fission on x-axis
    
    for i in range(0,2):# values for two secondary neutrons
        c=random.random()
        k=int(1*c)
        if c>0.5:#condition for neutron to be travelling to the right
            mr[k]=mr[k]+1#adds 1 to the bin for secondary neutrons travelling right
            ff=ff+R
            if 0<=ff<l:#condition for secondary fission from neutrons travelling right
                sf[k]=sf[k]+1#adds 1 to bin for secondary fissions
        else:#condtion for neutron to be travelling to the left
            ml[k]=ml[k]+1#adds 1 to bin for secondary neutrons travelling left
            ff=ff-R
            if 0<=ff<=l:#condition for secondary fission from neutrons travelling left
                sf[k]=sf[k]+1
                    
        
print mr , '1st secondary neutron moving right'
print ml , '1st secondary neutron moving left'
print sf , 'Number of secondary fission events that occur inside the bar'
        