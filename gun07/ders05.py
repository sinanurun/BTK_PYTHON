class Calisan:
    sirket = "BTK"
    def __init__(self,ad,soyad,maas):
        self.ad= ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.f_eposta()


    def f_eposta(self):
        return self.ad + self.soyad + "@sirket.com"

    @classmethod
    def pi(cls):
        return 3.14

print(Calisan.sirket)
calisan1 = Calisan("Enes","Meselik",50000)
print(calisan1.sirket)
print(calisan1.ad)
print(calisan1.maas)
calisan1.maas *= 1.5
print(calisan1.maas)
calisan1.sirket = "Aselsan"
print(calisan1.sirket)
print(Calisan.sirket)
Calisan.sirket = "THY"
print(Calisan.sirket)
print(calisan1.sirket)
calisan2 = Calisan("Gulce","GOK",50000.5)
print(calisan2.sirket)
print(calisan1.eposta)
print(calisan1.pi())
print(Calisan.pi())
