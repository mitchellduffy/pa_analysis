
# -*- coding: utf8 -*-


import spanish
import string
import numpy as np

class Measurement:
    def __init__(self, f):

        handle = open(f)

        lines = handle.readlines()
        x = 0

        for line in lines:

            x = x + 1

            line = line.split()

            if line[0] == 'Fecha:':
                self.date = spanish.makedatetime(line[1:])

            elif line[0] == 'Nombre':
                self.filename = line[3]

            elif line[0] == 'Muestra:':
                if len(line) < 2:
                    sys.exit('Error: Which sample is this: %s' % filename)
                elif len(line) == 2:
                    self.sample = line[1]
                else:
                    self.sample = string.join(line[1:])

            elif line[0] == 'Disolvente:':
                self.solvent = line[1]

            elif line[0] == 'Comentario:':
                self.comment = ''
                if len(line) == 2:
                    self.comment = line[1]
                elif len(line) > 2:
                    self.comment = string.join(line[1:])

            elif line[0][:9] == 'Observaci':
                self.wavelength = int(float(line[2]))

            elif line[0] == 'Temperatura':
                self.temperature = int(line[2])

            elif line[0] == 'Medida':
                self.energy = float(line[2].replace(',', '.'))

            elif line[0] == 'Tiempo':
                break


        self.data = np.zeros(shape=(len(lines[x:]), 3))

        i = 0
        for line in lines[x:]:
            nums = line.split()
            for y in range(3):
                self.data[i][y] = float(nums[y].replace(',', '.'))
            i += 1



        #print ''
        #print ''
        #print 'date'
        #print self.date
        #print 'filename'
        #print self.filename
        #print 'sample'
        #print self.sample
        #print 'solvent'
        #print self.solvent
        #print 'comment'
        #print self.comment
        #print 'wavelength'
        #print self.wavelength
        #print 'temperature'
        #print self.temperature
        #print 'energy'
        #print self.energy

    def process(self):
        index = np.argwhere(self.data[:, 0] == 4)[0][0]
        offset = np.argmax(self.data[index:, 1])
        y = self.data[index+offset, 1]
        x = self.data[index+offset, 0]
        self.sig1max = (x, y)

        offset = np.argmin(self.data[index:, 1])
        y = self.data[index+offset, 1]
        x = self.data[index+offset, 0]
        self.sig1min = (x, y)

        offset = np.argmax(self.data[index:, 2])
        y = self.data[index+offset, 2]
        x = self.data[index+offset, 0]
        self.sig2max = (x, y)

        offset = np.argmin(self.data[index:, 2])
        y = self.data[index+offset, 2]
        x = self.data[index+offset, 0]
        self.sig2min = (x, y)

        self.raw1diff = self.sig1max[1] + self.sig1min[1]
        self.raw2diff = self.sig2max[1] + self.sig2min[1]
        self.rawavgdiff = (self.raw1diff + self.raw2diff)/2
        self.energyavgdiff = self.rawavgdiff/self.energy
