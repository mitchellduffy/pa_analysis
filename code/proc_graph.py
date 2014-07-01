
import graphcollect
import matplotlib.pyplot as plt
import operator

class ProcGraph:

    def __init__(self, ml, sig, norm, ener):
        self.ml = ml
        signal = graphcollect.GraphCollect(ml, sig)
        self.title = signal.title
        if norm > -1:
            normalize = graphcollect.GraphCollect(ml, norm)
            if ener > 0:
                self.final = (signal.wavelengths, map(operator.sub, signal.energydiffs, normalize.energydiffs))

            else:
                self.final = (signal.wavelengths, map(operator.sub, signal.avgdiffs, normalize.avgdiffs))

        elif (norm <= -1 and ener > 0):
            self.final = (signal.wavelengths, signal.energydiffs)

        else:
            self.final = (signal.wavelengths, signal.avgdiffs)

        self.plotme()



    def plotme(self):
        plt.plot(self.final[0], self.final[1])
        plt.suptitle(self.title)
        plt.show(block=True)







