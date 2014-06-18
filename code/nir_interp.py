#interpolates wavelength (nm) of Near Infrared Signal into the setting on the micrometer given the current calibration curve.
#The equation for interpolation is a third degree polynomial that was regressed using Excel.


import math


for x in range(730, 1001, 5):

    y = (2.5467e-8 * x**3) - (7.6449e-5 * x**2) + (6.9213e-2 * x) - 9.5582
    z = y - math.fmod(y, .5)
    zz = math.fmod(y, .5)*100.0
    print str(x) + " | " + str(z) + "   " + str(zz)



