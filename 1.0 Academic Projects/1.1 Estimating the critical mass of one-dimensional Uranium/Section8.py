##Monte Carlo Simulation- Model for one dimensional uranium ##

from numpy import random,zeros

l=100# length of uranimum x-axis units cm

a=1.7 #mean free path between the neutron hitting another nucleus and bouncing off units cm
b=21#mean free path between neutron hitting a nucleus and causing fission
R=(2*a*b)**(0.5)#RMS distance a neutron moves before causing fission

mr=zeros(1,float)#bin for 1st secondary neutron moving right
ml=zeros(1,float)#bin for 1st seconday neutron moving left
nr=zeros(1,float)#bin for 2nd seconday neutron moving right
nl=zeros(1,float)#bin for 2nd secondary neutron moving left
sf=zeros(1,float)#bin for number of secondary fission events

x=1
while x<=100:#perform iteration 100 times
    ff=l*random.random()#produces value for intial fission on x-axis
    
    for i in range(1,2,1):#first of the seconday neutrons
        if i==1:
            c=random.random()
            k=int(1*c)
            if c>0.5:#condition for neutron to be travelling to the right
                mr[k]=mr[k]+1#adds 1 to the bin for 1st secondary neutron travelling right
                if (ff+R)>l:#condition for secondary fission from neutrons travelling right
                    sf[k]=sf[k]+1#adds 1 to bin for secondary fissions
            else:#condtion for neutron to be travelling to the left
                ml[k]=ml[k]+1#adds 1 to bin for 1st secondary neutron travelling left
                if (ff-R)>l:#condition for secondary fission from neutrons travelling left
                    sf[k]=sf[k]+1
                
    for i in range(1,2,1):#second, secondary neutron          
        if 1==1:
            d=random.random()
            k=int(1*d)
            if d>0.5:
                nr[k]=nr[k]+1
                if (ff+R)>l:
                    sf[k]=sf[k]+1
            else:
                nl[k]=nl[k]+1
                if (ff-R)>l:
                    sf[k]=sf[k]+1
            
    x=x+1     
        
print mr , '1st secondary neutron moving right'
print ml , '1st secondary neutron moving left'
print nr , '2nd secondary neutron moving right'
print nl , '2nd econdary neutron moving left'
print sf , 'Number of secondary fission events that occur inside the bar'





        