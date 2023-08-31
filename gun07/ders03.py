class Ogrenci:
    bolum =    "Mühendislik"
    def __init__(self):
        self.ad = 'Halit'
        self.soyad = ''

ogr1 = Ogrenci()
print(ogr1.ad)
print(ogr1.bolum)
print(Ogrenci.bolum)

