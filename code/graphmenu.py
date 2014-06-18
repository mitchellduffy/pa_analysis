
import sys
import graphll
import proc_graph


class GraphMenu:

    def __init__(self, ml):
        self.ml = ml
        self.namelist = []
        for folder in self.ml.cabinet:
            self.namelist.append((folder[0].sample, folder[0].comment))
        self.topmenu()

    def display_namelist(self):
        i = 0
        for name in self.namelist:
            print str(i) + '. ' + name[0] + '\n\t' + name[1]
            i += 1
        print ''

    def topmenu(self):

        self.sig = -1
        self.norm = -1
        self.ener = -1

        print ''
        print 'MAIN MENU'
        print 'How would you like to analyze the data?:'
        print ''
        print '0. RAW graphs with Max/Min plotted'
        print '1. RAW spectra'
        print '2. Blank Normalized spectra'
        print '3. Energy Normalized spectra'
        print '4. Blank and Energy Normalized spectra'
        print ''
        print '5. Exit'
        print ''
        ans = self.saninput('Input: ', 5)

        if ans == 5:
            print ''
            print 'Ciao'
            print ''
            sys.exit(0)
        elif ans == 0:
            ll = graphll.GraphLL(self.ml)
        elif ans > 0:
            self.sig = self.which('Signal')

            if ans == 2 or ans == 4:
                self.norm = self.which('Blank Normalization')

            if ans > 2:
                self.ener = 1

        p = proc_graph.ProcGraph(self.ml, self.sig, self.norm, self.ener)

        self.topmenu()







    def which(self, t):
        print ''
        print 'Which sample would you like to use as ' + t
        print ''
        self.display_namelist()
        print ''
        print str(len(self.namelist)) + '. Back to Main Menu'
        print ''

        ans = self.saninput('Input: ', len(self.namelist) - 1 + 1)
        if ans == len(self.namelist):
            self.topmenu()
        else:
            return ans



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








