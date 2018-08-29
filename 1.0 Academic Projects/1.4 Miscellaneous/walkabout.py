from physics import *
import pylab

def get_histogram(nwalks, n):
	"Computes histogram of nwalks walks on n steps"
	jmax=NBINS-1                        # Size of array containing distances
	deltaR=(1.1*n)/jmax
	m=zeros(NBINS, int)
	for k in range(1, nwalks+1):        # Count walks
		R=distance(n)                   # Determine distance from start
		j=int(floor(R/deltaR+0.5))      # Convert to bin number
		if j<jmax: m[j]+=1              # Increment count of distance bin
	
	return m

#----------------------------------------------------------------------------

def distance(n):
	"Computes distance moved after n random steps"
	x=0; y=0; z=0                       # Start at origin
	for i in range(0,n):                # Count steps
		c=2.0*uniform(1)-1.0            # c=cos(theta)
		s=sqrt(1.0-c*c)                 # s=sin(theta)
		phi=2.0*pi*uniform(1)           # phi is random azimuth
		x+=s*cos(phi)                   # calculate new position
		y+=s*sin(phi)
		z+=c
	
	return sqrt(x*x+y*y+z*z)            # final distance from origin

#----------------------------------------------------------------------------

def P(r):
	"Computes the theoretical expression for P(r)"
	global glob_r
	glob_r=r       # copies r to global variable to get value into f(x)
	return (2*r/pi)*gaussint(0, upper_limit, 1e-3)

#----------------------------------------------------------------------------

def f(x):
	"This is integrand, r and n are got from global variables"
	y=sin(x)/x
	z=sin(glob_r*x)*x
	for i in range(1, glob_n+1): z*=y
	return z

#----------------------------------------------------------------------------

def g(r, n):        # This keeps the notation P for the function computed
	return P(r)     # and g for the function plotted. n is not needed.

#-----------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------

global glob_n, upper_limit
NBINS=20
n=3                                       # Number of steps
glob_n=n
nwalks=10000                              # Number of walks
deltaR=(1.1*n)/(NBINS-1)

# This upper limit must be float to force subsequent types to be float
upper_limit=50.0                          # Upper limit for integration

m=get_histogram(nwalks, n)                # Compute histogram

x=zeros(NBINS, float); y=zeros(NBINS, float); e=zeros(NBINS, float)
th=zeros(NBINS, float)
for i in range(0,NBINS):
	x[i]=i*deltaR                         # Get true r from bin number
	y[i]=m[i]/(nwalks*deltaR)             # Estimate P(r) from histogram
	e[i]=sqrt(m[i])/(nwalks*deltaR)       # Error from Poisson statistics
	th[i] = g(x[i],0) 

pylab.errorbar(x,y,e)
pylab.plot(x,th)
pylab.show()

# xyplot(x, y, e, NBINS-1, 13)              # Plot points, errorbars and theory
