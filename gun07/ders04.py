class Ogrenci:
    bolum = "Mühendislik"
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad

    def tamad(self):
        tam_isim = self.ad + self.soyad
        return tam_isim

ogr1 = Ogrenci("Halit","Tirsi")
print(ogr1.ad)
print(ogr1.tamad())

ogr2 = Ogrenci("Semih","Ocak")
print(ogr2.ad)
