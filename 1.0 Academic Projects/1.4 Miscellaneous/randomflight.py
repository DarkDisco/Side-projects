# -*- coding: utf-8 -*-
from physics import *
import pylab

def distance(n):
	"Computes distance moved after n random steps"
	x=y=z=0                             # Start at origin
	for i in range(0,n):                # Count steps
		c=2.0*uniform(1)-1.0            # c=cos(theta)
		s=sqrt(1.0-c*c)                 # s=sin(theta)
		phi=2.0*pi*uniform(1)           # phi is random azimuth
		x+=s*cos(phi)                   # calculate new position
		y+=s*sin(phi)
		z+=c
	
	return sqrt(x*x+y*y+z*z)            # final distance from origin

#----------------------------------------------------------------------------

nbins=50
jmax=nbins-1                            # Size of array containing distances
n=3                                     # Number of steps
nwalk=1000
deltaR=(1.1*n)/jmax
m=[0 for i in range(0,jmax)]            # Zero array 
for k in range(0,nwalk):                # Count walks
	R=distance(n)                       # Determine distance from start
	j=int(floor(R/deltaR+0.5))          # Convert to bin number
	if j<jmax: m[j]+=1                  # Increment count of distance bin

pylab.bar(range(len(m)),m,width=1.)
pylab.show()


