

class GraphMenu:

    def __init__(self, ml):
        self.namelist = []
        for folder in ml.cabinet:
            self.namelist.append((folder[0].sample, folder[0].comment))
        self.topmenu()

    def display_namelist(self):
        i = 0
        for name in self.namelist:
            print str(i) + '. ' + name[0] + '\n\t' + name[1]
            i += 1
        print ''

    def topmenu(self):
        print 'How would you like to analyze the data?:'
        print '0. RAW graphs with Max/Min plotted'
        print '1. RAW spectra'
        print '2. Blank Normalized spectra'
        print '3. Energy Normalized spectra'
        print '4. Blank and Energy Normalized spectra'
        self.display_namelist()
        ans = self.saninput('Which sample whould you like to analyze? \n', len(self.namelist) - 1)
        self.wantnorm(ans)


    def saninput(self, s, b):
        try:
            x = int(raw_input(s))
        except ValueError:
            print "Error: input wasn't an integer\n"
            x = self.saninput(s, b)
        if x > b or x < 0:
            print 'Error: number out of bounds. Choose a number from the menu.\n'
            x = self.saninput(s, b)
        else:
            return x

    def wantnorm(self, samp):
        print '0. Yes\n1. No'
        ans = self.saninput('Would you like to normalize the data?', 1)
        if ans == 0:
            self.display_namelist()
            norm = self.saninput('Which dataset should be used for normalization?', len(self.namelist) - 1)
        else:
            norm = -1







