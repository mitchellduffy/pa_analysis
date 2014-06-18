
import sys
import os
import measure_list
import measurement
import graphll
import graphmenu

if len(sys.argv) < 2:
    sys.exit('Usage: %s dir' % sys.argv[0])

path = sys.argv[1]

if not os.path.exists(path):
    sys.exit('Error: Directory %s was not found' % path)

if not os.path.isdir(path):
    sys.exit('Error: %s is not recognized as a valid directory' % path)

print 'Photoacoustic Data Analysis Software'
print 'Author: Mitchell Duffy'
print 'License: MIT License'
print ''
print 'Building Database...'
print 'For large directories this may take a few minutes.'
print ''


ml = measure_list.MeasureList()

for i in os.listdir(path):
    if not i.endswith('.txt'):
        continue
    else:

        m = measurement.Measurement(path + i)

        m.process()

        ml.organize(m)

# This fuction is used to check the max/min of each graph in a series
#graphll.graphme(ml)

menu = graphmenu.GraphMenu(ml)


