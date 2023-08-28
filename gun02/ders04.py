#turnava deneyimi
boy = int(input("Boy bilgisini giriniz"))
okul = input("Üni öğrencisi misin")
if okul == "evet" and (boy > 180 or boy == 180) :
    print("Turnuvaya katılabilirsiniz")
else:
    print("turnuvaya katılamazsınız")