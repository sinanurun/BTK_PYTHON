class Calisan:
    zam_oranı = 1.1
    per_say = 0
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad + self.soyad + "@sirket.com"
        Calisan.per_say = Calisan.per_say + 1
    def tamad(self):
        return "adı : {}  soyadı : {}".format(self.ad, self.soyad)
    def arttir(self):
        # self.maas = (self.maas*1.05)
        # self.maas = (self.maas * Calisan.zam_oranı)
        self.maas = (self.maas * self.zam_oranı)
print(Calisan.per_say)
personel1 = Calisan("Ali","Demir",2500)
print(Calisan.per_say)
personel2 = Calisan("Kerim","Bakır",2000)
# print(Calisan.per_say)
personel1.arttir()
print(personel1.maas)
personel2.zam_oranı = 1.15
personel2.arttir()
print(personel2.maas)
