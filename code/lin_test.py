
import sys
import os
import measure_list
import measurement
import graphll
import graphmenu
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    sys.exit('Usage: %s dir' % sys.argv[0])

path = sys.argv[1]

if not os.path.exists(path):
    sys.exit('Error: Directory %s was not found' % path)

if not os.path.isdir(path):
    sys.exit('Error: %s is not recognized as a valid directory' % path)

print 'Photoacoustic Data Analysis Software'
print 'Linear Check'
print 'Author: Mitchell Duffy'
print 'License: MIT License'
print ''
print 'Building Database...'
print ''


ml = measure_list.MeasureList()

for i in os.listdir(path):
    if not i.endswith('.txt'):
        continue
    else:

        m = measurement.Measurement(path + i)

        m.process()

        ml.organize(m)


r = []
for [m] in ml.cabinet:
    r.append((m.energy, m.rawavgdiff))
    #r.append(int(m.comment.split()[0][:-1]))

r = sorted(r, key=lambda tup:tup[0])

x = [tup[0] for tup in r]
y = [tup[1] for tup in r]

print x
print y


plt.plot(x, y, 'ro')
plt.show(block=True)


