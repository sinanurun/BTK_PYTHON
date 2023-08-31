class Calisan:

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

    @classmethod
    def zam_orani_degis(cls,yeni_oran):
        cls.zam_oranı = yeni_oran

    @classmethod
    def ypersonel(cls,pbilgisi):
        ad, soyad, maas = pbilgisi.split("-")
        return cls(ad,soyad,maas)

    @staticmethod
    def tel_no(telefon):
        return telefon.split(" ")

print(Calisan.tel_no("0555 555 55 55"))


personel1 = Calisan("Ali", "Demir", 2500)
personel2 = Calisan("Kerim","Bakır",2000)
personel1.arttir()
print(personel1.maas)
print(personel1.zam_oranı)
Calisan.zam_orani_degis(1.2)
print(personel1.zam_oranı)
print(personel2.zam_oranı)
print(Calisan.zam_oranı)

mpersonel1 = "Sonay-Karaaslan-55000"

yeni_personel = Calisan.ypersonel(mpersonel1)
print(yeni_personel.ad)
