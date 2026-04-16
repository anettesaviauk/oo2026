import math


class Kalkulaator:
    sisu= '0'
    def vajutus(self,nupp):
        if self.sisu == '0':
            self.sisu = nupp
        else:
            self.sisu += nupp
    def ekraan(self):
        return self.sisu
    def sin(self):
        self.sisu
        numbrid = list(self.sisu.split('sin'))
        ##print (result)
        result = int(numbrid[0])
        self.sisu = math.sin(math.radians(result))
    def liitmine(self):
        self.sisu
        result = sum(int(x) for x in self.sisu.split('+'))
        ##print (result)
        self.sisu= str(result)
    def lahutamine(self):
        numbrid = [int(x) for x in self.sisu.split('-')]
        tulemus = numbrid[0]
        for arv in numbrid[1:]:
            tulemus -= arv
        self.sisu= str(tulemus)
    def korrutamine(self):
        self.sisu
        numbrid = (int(x) for x in self.sisu.split('*'))
        ##print (result)
        result = math.prod(numbrid)
        self.sisu= str(result)
    def jagamine(self):
        self.sisu
        numbrid = [int(x) for x in self.sisu.split('/')]
        tulemus = numbrid[0]
        # Käime läbi kõik arvud alates teisest
        for arv in numbrid[1:]:
            if arv == 0:
                self.sisu = "Viga: nulliga jagamine"
                return
            result /= arv
            self.sisu=str(result)
    def jagamine(self):
        numbrid = [int(x) for x in self.sisu.split('/')]
        tulemus = numbrid[0]
        for arv in numbrid[1:]:
            if arv == 0:
                self.sisu = "Viga: nulliga jagamine"
                return
        tulemus /= arv
        if tulemus == int(tulemus):
            tulemus = int(tulemus)
            self.sisu = str(tulemus)