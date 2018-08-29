import matplotlib.pyplot as plt
import numpy

"""for n in range(1,5):
    x = numpy.linspace(-5,5,num=400)
    series = numpy.cos(1e4/n*x)
    plt.figure()
    plt.plot(series)"""

def quadratic(a, b, c):
	import math
	return [((-b + i * math.sqrt(b*b - 4*a*c)) / (2 * a)) for i in (-1, 1)]

print quadratic(0.01,100,-0.01)

z=[b*b, 4*a*c, math.sqrt(b*b - 4*a*c), 2*a, math.sqrt(b*b - 4*a*c)/(2*a)]
print z, len()