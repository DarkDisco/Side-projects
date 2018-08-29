def gaussint(f,a, b, delta, args=()):
  "Integrates f(x) between a and b with accuracy delta"
  n=8
  f1=I(f, n, a, b, args=args)
  f2=-f1
  while abs(f2-f1) > delta*abs(f1):
    if (n==16384):
      print "Can't achieve accuracy requested"
      return 0
    f2=f1
    n=2*n
    f1=I(f, n, a, b, args=args)
  return f1

#---------------------------------------------------------------------------*/

def I(f, n, a, b, args=()):
  "Divides range a to b into n panels"
  h=(b-a)/n
  sum=0.0
  for i in range(0,n):
    sum+=tenpoint(f, a+i*h, a+(i+1)*h, args=args)
  return sum

def tenpoint(f, a, b, args=()):
  "Evaluates integral from a to b by 10 point Gauss formula"
  u=0.5*(a+b); v=0.5*(b-a)
  s=0.2955242247*(f(u+0.1488743389*v,*args)+f(u-0.1488743389*v,*args))+ \
    0.2692667193*(f(u+0.4333953941*v,*args)+f(u-0.4333953941*v,*args))+ \
    0.2190863625*(f(u+0.6794095682*v,*args)+f(u-0.6794095682*v,*args))+ \
    0.1494513491*(f(u+0.8650633666*v,*args)+f(u-0.8650633666*v,*args))+ \
    0.0666713443*(f(u+0.9739065285*v,*args)+f(u-0.9739065285*v,*args))
  return 0.5*s*(b-a)


#---------------------------------------------------------------------------*/
from math import sin, pi

def sxox(x):
  return sin(x)/x

def f(x,r,n):
  "Integrand for random walk displacement distribution"
  return x*sin(r*x)*(sin(x)/x)**n

print 'Integrating sin(x)/x'
print gaussint(sxox, 0.0, 10000.0, 1.0e-6), pi/2
r=2.5
n=3
print 'Integral for P(r) for r=%f and n=%d, varying upper limit' % (r,n)
print '%5s  %s' % ('upper','P(r)')
for upper in (10.0,20.0,40.0,80.0,160.0,320.0,640.0):
 print '%5.1f  %f' % (upper,
                      (2.0*r/pi)*gaussint(f,0.0,upper,1.0e-6,args=(r,n)))
