from physics import *

def gaussint(a, b, delta):
	"Integrates f(x) between a and b with accuracy delta"
	n=8
	f1=I(n, a, b)
	f2=-f1
	while abs(f2-f1) > delta*abs(f1):
		if (n==16384):
			print "Can't achieve accuracy requested"
			return 0
		
		f2=f1
		n=2*n
		f1=I(n, a, b)
	
	return f1

#---------------------------------------------------------------------------*/

def I(n, a, b):
	"Divides range a to b into n panels"
	h=(b-a)/n
	sum=0.0
	for i in range(0,n):
		sum+=tenpoint(a+i*h, a+(i+1)*h)
	return sum

def tenpoint(a, b):
	"Evaluates integral from a to b by 10 point Gauss formula"
	u=0.5*(a+b); v=0.5*(b-a)
	s=0.2955242247*(f(u+0.1488743389*v)+f(u-0.1488743389*v))+ \
      0.2692667193*(f(u+0.4333953941*v)+f(u-0.4333953941*v))+ \
      0.2190863625*(f(u+0.6794095682*v)+f(u-0.6794095682*v))+ \
      0.1494513491*(f(u+0.8650633666*v)+f(u-0.8650633666*v))+ \
      0.0666713443*(f(u+0.9739065285*v)+f(u-0.9739065285*v))

	return 0.5*s*(b-a)

#---------------------------------------------------------------------------*/

def f(x):
	"This defines the function to be integrated"
	return sin(x)/x

print gaussint(0.0, 1000.0, 1.0e-6), pi/2
