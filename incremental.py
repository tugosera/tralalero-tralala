class Patsient:
    def __init__(self,nimi,vanus):
        self.nimi = nimi
        self.vanus = vanus
        self.regAeg = ""

class Haigla:

    patsiendiList = []
    arstidelist = []

    def patsienditeKuuvamine(self, patsiendiList):
        patsiendiList = patsiendiList
        for index,elem in enumerate(patsiendiList):
            print('id: ',index, 'Nimi: ', elem.nimi, 'Vanus: ',elem.vanus)

    def patsienditeKuuvamine(self, arstidelist):
        arstidelist = arstidelist
        for index,elem in enumerate(arstidelist):
            print('id: ',index, 'Nimi: ', elem.nimi, 'Vanus: ',elem.vanus)

    def kohtumineTegemine(self):
        patsiendiIndex = 0
        patsientiNimi = input("sisesta patsientiNimi")
        arstiNimi = input("sisesta arstiNimi")
        for elem in self.patsiendiList:
            if elem.nimi == patsientiNimi:
                patsientiIndex = patsiendiList.index(elem)
        
        for elem in self.arstidelist:
            if elem.nimi == patsientiNimi:
                patsientiIndex = patsientiList

        




class Arst:
    def __init__ (self,nimi,vanus,eriala,aeg):
        self.nimi = nimi
        self.vanus = vanus
        self.eriala = eriala
        self.aeg = aeg

Patsient1 = Patsient("Thomas", 77)
Patsient2 = Patsient("Vladek", 18)
Patsient3 = Patsient("Sashko", 17)
arst1 = Arst("Muhamad", 25, "alergoolog",['10.00', '12.00', '14.00'])
haigla = Haigla()

haigla.patsiendiList.append(Patsient1) 
haigla.patsiendiList.append(Patsient2)
haigla.patsiendiList.append(Patsient3)
haigla.arstidelist.append(arst1)

haigla.patsienditeKuuvamine(haigla.patsiendiList)