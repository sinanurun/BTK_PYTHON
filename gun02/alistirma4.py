egitim = int(input("1 (ilkokul),2,3,4 seçiniz"))
if egitim >1 :
    yas =int(input("yaşınızı giriniz"))
    print("ehliyet alabilirsiniz") if yas >= 18 else print("ehliyet alamazsınız")
else:
    print("Eğitim yeterliliğiniz ehliyete yetmiyor")