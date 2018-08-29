from physics import *
import pylab as py
import numpy as np

def f(x):
    "sums Fourier series"
    total=0.0    
    term=1.0
    n=1
    m=3
    o=1 
    
    while abs(term) > 1e-5 * (abs(total)+1e-4):
        term=np.sin(n*x)/n
        n=n+2.0
        total=total+term
        
        return total
    
"""
    while abs(term) > 1e-5 * (abs(total)+1e-4):
        term = np.cos( n * x ) / ( n * n )
        n = n + 2.0
        total = total + term
        
        return total

    
    while abs(term) > 1e-5 * (abs(total)+1e-4):
        term=np.cos(2*n*x)*(-1)/(o*m)
        n=n+1.0
        m=m+2.0
        o=o+2.0
        total=total + term

        return 0.5 + total"""
    

    

        
n=500   
g=[f((4*pi*i)/n) for i in range(0,n)]
    
py.plot(g)
py.show()