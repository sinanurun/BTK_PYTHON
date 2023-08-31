class Sporcu():
    total_bornz = 5
    _total_gumus = 15
    __total_madalya = 25
    def __init__(self,ad,brans,altin,gumus,bronz):
        self.ad = ad
        self.brans = brans
        self.mbronz = bronz #public veri halka açık değişken
        self._mgumus = gumus #protected yarı gizli
        self.__maltin = altin #private tam gizli
    def atlet_bilgisi(self):
        return "Sporcu adı : {}, Branşı :{}".format(atlet1.ad,atlet1.brans)
    @property
    def a_yazdir(self):
        amadalya = self.__maltin
        return "altın madalya sayısı {}".format(self.__maltin)

class Gsporcu(Sporcu):
    def __init__(self,ad,brans,altin,gumus,bronz):
        super().__init__(ad,brans,altin,gumus,bronz)

    def fbmyazdir(self):
        print("Bronz",self.mbronz)

    def fgmyazdir(self):
        print("gümüş", self._mgumus)
    def famyazdir(self):
        print("Altın", self.__maltin)

class Torun(Gsporcu):
    def __init__(self,ad,brans,altin,gumus,bronz):
        super().__init__(ad,brans,altin,gumus,bronz)

    def fbmyazdir(self):
        print("Bronz",self.mbronz)

    def fgmyazdir(self):
        print("gümüş", self._mgumus)
    def famyazdir(self):
        print("Altın", self.__maltin)



# atlet1 = Sporcu("ali","100 Metre",2,3,9)
# print(atlet1.atlet_bilgisi())
# print("bronz madalya sayısı",atlet1.mbronz)
# print("gümüş madalya sayısı",atlet1._mgumus)
# # print("Altın Madalya",atlet1.__maltin)
# print(atlet1.a_yazdir)
# gatlet = Gsporcu("ali","100 Metre",2,3,9)
# gatlet.fbmyazdir()
# gatlet.fgmyazdir()
# gatlet.famyazdir()

torun = Torun("ali","100 Metre",2,3,9)
# torun.fbmyazdir()
# torun.fgmyazdir()
# torun.famyazdir()
# print(torun.total_bornz)
# print(torun._total_gumus)
# print(torun.__total_altin)

print(Torun.total_bornz)
print(Torun._total_gumus)
print(Torun.__total_altin)




