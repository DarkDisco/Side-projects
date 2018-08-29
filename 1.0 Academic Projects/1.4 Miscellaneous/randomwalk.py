import numpy as np
import pylab as py
from physics import *

"""def walk(n):
    x=y=0
    random=rand(100,10,1234567, (2**31)-1)
    phi=2.0*pi*uniform(1)
    l=[]
    for i in range(0,100):
        w=random[i]/e9
        i+=1
        l.append(w)
    
    
    
    
    return l
    
#print l[n]
#py.plot(l,l)
print l"""
n=10
x=[0,]
y=[0,]

for i in range(0,4,1):

    xstep=random.randint(0,10)
    ystep=random.randint(0,10)
    x0=y0=0
    xterm=x0+xstep
    yterm=y0+ystep
    n+=1

    x.append(xterm)
    y.append(yterm)


py.plot(x,y)