

class GraphCollect:

    def __init__(self, ml, index):
        tuples = []
        a = ml.cabinet[index]
        for x in a:
            tuples.append((x.wavelength, x.rawavgdiff, x.energyavgdiff))
        tuples = sorted(tuples, key=lambda tup: tup[0])
        self.wavelengths = [tup[0] for tup in tuples]
        self.avgdiffs = [tup[1] for tup in tuples]
        self.energydiffs = [tup[2] for tup in tuples]
        self.title = a[0].comment



