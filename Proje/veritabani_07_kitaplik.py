import sys
import veritabani_06 as baglanti
print("-"*56)
print("-"*10, "Kitaplık Programımıza Hoş Geldiniz", "-"*10)
print("-"*56)

k_id = 0

while 1 == 1:
    while k_id == 0:
        eposta = input("Kullanıcı e posta giriniz")
        sifre = input("kullanıcı şifre giriniz")
        k_id = baglanti.k_giris(eposta,sifre)
        if k_id == 0 :
            continue
        else:
            break

    print("-"*10, "Yapmak istediğiniz işlemi Seçiniz", "-"*10)
    print("-" * 10, "(E)klemek,(L)istelemek,(G)üncellemek,(S)ilmek,(Ç)ıkmak", "-" * 10)

    islem = input()
    if islem == "Ç" or islem == "ç":
        baglanti.cikis()
        sys.exit()
    elif islem == "E" or islem == "e":
        kitap = input("kitap adını giriniz")
        yazar = input("kitap yazarını")
        okunma = input("kitap okunma durumunu giriniz")
        begeni = input("kitap beğeni değerini giriniz")
        baglanti.ekle(k_id,kitap, yazar, okunma, begeni)
    elif islem == "L" or islem == "l":
        baglanti.listele(k_id)
    elif islem == "G" or islem == "g":
        baglanti.listele(k_id)
        guncellenecek = input("güncellemek istediğiniz kitabın id'sini giriniz")
        baglanti.guncelle(guncellenecek)
    elif islem == "S" or islem == "s":
        baglanti.listele(k_id)
        silinecek = input("silmek istediğiniz kitabın id'sini giriniz")
        baglanti.sil(silinecek)