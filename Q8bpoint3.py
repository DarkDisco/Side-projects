##Monte Carlo Simulation- Model for one dimensional uranium, upadte using neutrons() ##

from numpy import random,zeros
from neutrons import neutrons

w=zeros(10,int)
"""Each bin counts the amount of times the code finds a ratio of at least 1 
for a given value of L between the upper and lower bounds. The outer loop runs
the code 100 times and the bin with the smallest index equal 100 is the value
for L which fits my criteria."""

for v in range(0,100,1):#Runs code 100 times to average out random error 
    aa=[]               #associated with the number of neutrons that cause
    bb=[]               #secondary fissions.
    cc=[]
    p=[]#Will containe the final value of L
    lb=10#lower bound for values of L that could be the  critcial length
    ub=20#upper bound for values of L 
    
    
    for l in range(lb,ub,1):#runs inner loops over a range of L values
        a=1.7 #mean free path between the neutron hitting another nucleus and bouncing off units cm
        b=21#mean free path between neutron hitting a nucleus and causing fission
        R=(2*a*b)**(0.5)#RMS distance a neutron moves before causing fission
        
        mr=zeros(1,float)#bin for secondary neutrons moving right
        ml=zeros(1,float)#bin for secondary neutrons moving left
        sf=zeros(1,float)#bin for number of secondary fission events
        junk=zeros(1,float)#bin for ratios of secondary fissions per initial less than 1
        
        
        
        
        for i in range(0,1000):#number of initial fissions
            ff=l*random.random()#produces value for position ofintial fission on x-axis
        
            for i in range(0,neutrons()):# values for two secondary neutrons
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
        aa.append(mr)#converts the bin values for electrons moving right each loop to a list
        bb.append(ml)#converts the bin values of electrons moving left each loop to a list
        cc.append(sf)  #converts the bin value for number of secondary fissions each loop to list  
                    
    ee=[]#list for converted array values from cc into integers

    for i in range(0,10,1):#converting array values into integer list
        ee.append(int(cc[i]))

    ps=ee[0] ; o=0
    for i in range(0,len(ee)):#finds the fist value that will give a ratio of 1 
        if ee[i]>=1000:
            ps=ee[i] ; o=1
            w[i]=w[i]+1 
            
mx=w[0] ; v=0
for i in range(0,len(w)):#finds 1st value of w equal to 100 and 
    if w[i]>mx:
        mx=w[i] ; j=1
p.append(i+lb)

"""Have left in the print statments below as allows for great breakdown of the 
data at various steps of the code"""    
#print aa , 'no. neutrons travelling right for each value of L'
#print bb , 'no, neutrons travelling left for each value of L' 
#print cc , 'Number of seconadary fissions at each value of L'
#print ee , 'value for the no. secondary fissions'
#print w , 'bin value for how many times a given L value meet the criteria'
print p , """Value of L in cm that satisfied the criteria for being the 
critical length when simulation is repeated 100 times, with 1000 intial 
fissions.""" 
