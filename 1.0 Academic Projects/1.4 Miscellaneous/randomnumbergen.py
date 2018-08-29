import numpy as np
import pylab as py

a=1234567.
N=((2**31)-1)
xn=10
b=[]

def rand(n, xn, a, N):
    b=[]    
    for i in range(0,n):
        xn=(a*xn)%N
        b.append(xn)
    return b
    
n = 100
b, c = rand(n, 10, 1234567, (2**31)-1), rand(n, 10, 1234567, (2**31)-1)

b.pop()
c.pop(0)

py.plot(b,c, '.r',)
py.show()
print len(b)