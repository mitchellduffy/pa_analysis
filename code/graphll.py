
#graphs low level data


import matplotlib.pyplot as plt

class GraphLL:

    def __init__(self, ml):
        print ''
        print 'The graphs are rendered in another window.'
        print ''
        for folder in ml.cabinet:
            for littlefile in folder:
                self.single_graph(littlefile)


    def single_graph(self, d):
        x = d.data[:, 0]
        y = d.data[:, 1]
        z = d.data[:, 2]
        plt.plot(x, y)
        plt.plot(x, z)
        plt.plot([d.sig1max[0], d.sig1min[0]], [d.sig1max[1], d.sig1min[1]], 'ro')
        plt.plot([d.sig2max[0], d.sig2min[0]], [d.sig2max[1], d.sig2min[1]], 'bo')
        plt.suptitle(d.filename)

        plt.show(block=True)





