class Ogrenci():
    def __init__(self, ad, soyad):
        self.adi = ad
        self.soyad = soyad


class Fogrencisi(Ogrenci):
    def __init__(self, ad, soyad, fakulte):
        Ogrenci.__init__(self, ad, soyad)
        self.fakulte = fakulte


class BOgrencisi(Fogrencisi):
    def __init__(self, ad, soyad, fakulte, bolum):
        # Fogrencisi.__init__(self, ad, soyad, fakulte)
        super().__init__(ad, soyad, fakulte)
        self.bolum = bolum


genel_ogrenci = Ogrenci("ali", "veli")
print(genel_ogrenci.adi, genel_ogrenci.soyad)

fakulte_ogrencisi = Fogrencisi("Uğur", "YERSEL", "Mühendislik")
print(fakulte_ogrencisi.fakulte)

bolum_ogrencisi = BOgrencisi("Uğur","YERSEL","Mühendislik","Bilgisayar")
print(bolum_ogrencisi.bolum)
