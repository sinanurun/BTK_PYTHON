burger = int(input("1 tavuklu, 2 köfteli, 3 sebzeli, şeçim dışı 0 "))
patates = int(input("1 küçük, 2 orta, 3 büyük boy patates, şeçim dışı 0 "))
icecek = int(input("1 ayran, 2 kola, 3 soda, şeçim dışı 0 "))

tutar = 0
if burger == 1:
    tutar += 80
    burger = "Tavuklu"
elif burger == 2:
    tutar += 90
    burger = "Köfte"
elif burger == 3:
    tutar += 50
    burger = "Sebze"
else:
    burger = "Seçim Yapmadınız"

if patates == 1:
    tutar += 5
elif patates == 2:
    tutar += 10
elif patates == 3:
    tutar += 20

if icecek == 1:
    tutar += 10
elif icecek == 2:
    tutar += 50
elif icecek == 3:
    tutar += 15

siparis = """Siprarişiniz Hazır 
            Burger seçiminiz : {burger},
            Patates seçiminiz : {patates},
            İcecek Seçiminiz : {icecek},
            Toplam Hesabınız : {tutar}""".format(burger=burger, patates=patates,
                                                 icecek=icecek, tutar=tutar)
print(siparis)
