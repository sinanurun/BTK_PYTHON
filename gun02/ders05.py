#turnava deneyimi
boy = int(input("Boy bilgisini giriniz"))
if (boy >= 180) :
    okul = input("ünili misin")
    if okul == "evet":
        print("turnuvaya katılabilirsin")
    else:
        print("Okul durumunuz uygun değil")
else:
    print("Boy durumunuz uygun değil")
