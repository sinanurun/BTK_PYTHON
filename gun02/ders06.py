devamsizlik = int(input("Devamsızlık sayısını giriniz"))
if devamsizlik < 5 :
    disiplin = input("Disiplin cezanız var mı?")
    if disiplin == "Hayır":
        ortalama = int(input("Ortalamanınızı giriniz"))
        if 85<=ortalama:
            print("takdir aldınız")
        else:
            if 70 <= ortalama <85 :
                print("Teşekkür Aldınız")
            else:
                print("Belge alacak ortalamaya sahip değilsiniz")
    else:
        print("Disiplin durumunuz belge almaya engel")
else:
    print("Devamsizlik durumunuz belge almaya engel")