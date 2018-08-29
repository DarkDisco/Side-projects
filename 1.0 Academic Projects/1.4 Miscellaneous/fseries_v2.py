from physics import *
import pylab as py

def f(x):
	"Sums Fourier series"
	sum=0.0
	term=1.0
	n=1.0
	while abs(term) > 1e-5*(abs(sum)+1e-4):
		term=cos(n*x)/(n*n)
		n=n+2.0
		sum=sum+term

	return sum

#---------------------------------------------------------------------------

n=40
g=[f((4*pi*i)/n) for i in range(0,n)]

#graph(g)
py.plot(g)
py.show()
