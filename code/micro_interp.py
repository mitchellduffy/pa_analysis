
import math


for x in range(550, 691, 5):

    nir = 1.0/((1.0/355.0) - (1.0/float(x)))
    y = (2.6144e-7 * x**3) - (5.6475e-4 * x**2) + (0.40798 * x) - 88.384
    z = y - math.fmod(y, .5)
    zz = math.fmod(y, .5)*100.0
    print str(int(round(nir))) + " |  " + str(z) + " " + str(zz)



