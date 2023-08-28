devamsizlik = int(input("Devamsızlık sayısını giriniz"))
devamsizlik = devamsizlik < 5
if  devamsizlik:
    disiplin = input("Disiplin cezanız var mı?")
    disiplin = (disiplin == "Hayır")
    if disiplin:
        ortalama = int(input("Ortalamanınızı giriniz"))
        takdir = (85<=ortalama)
        tesekkür = (70 <= ortalama <85)
        if takdir:
            print("takdir aldınız")
        else:
            if tesekkür :
                print("Teşekkür Aldınız")
            else:
                print("Belge alacak ortalamaya sahip değilsiniz")
    else:
        print("Disiplin durumunuz belge almaya engel")
else:
    print("Devamsizlik durumunuz belge almaya engel")