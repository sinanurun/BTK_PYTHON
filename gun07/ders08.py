class Calisan():

    zam_oranı = 1.05
    per_say = 0

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
        Calisan.per_say = Calisan.per_say + 1
    def tamad(self):
        return "adı : {}  soyadı : {}".format(self.ad,self.soyad)

    def arttir(self):
        # self.maas = (self.maas*1.05)
        # self.maas = (self.maas * calisan.zam_oranı)
        self.maas = (self.maas * self.zam_oranı)

class gelistirici(calisan):
    def __init__(self,ad,soyad,maas,p_dili):
        # calisan.__init__(self,ad,soyad,maas)
        super().__init__(ad,soyad,maas)
        self.p_dili = p_dili
        self.zam_oranı = 1.2

class yonetici(Calisan):
    def __init__(self,ad,soyad,maas,calisanlar = None):
        super().__init__(ad,soyad,maas)
        if calisanlar is None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar

    def eleman_ekle(self,eleman):
        self.calisanlar.append(eleman)
    def eleman_cikar(self,eleman):
        self.calisanlar.remove(eleman)

    def calisan_listele(self):
        for eleman in self.calisanlar:
            print(eleman.tamad())