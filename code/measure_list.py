

class MeasureList:

    def __init__(self):
        self.cabinet = []

    def organize(self, m):
        if not self.cabinet:
            self.cabinet.append([m])
        else:
            added = False
            for item in self.cabinet:
                if (item[0].sample == m.sample) and (item[0].comment == m.comment):
                    item.append(m)
                    #print item
                    #print len(item)
                    added = True
                    break
            if added == False:
                self.cabinet.append([m])
