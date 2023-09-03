import sqlite3 as sql
vt = sql.connect('kitaplik_db.sqlite')
imlec = vt.cursor()

def kekle(eposta,sifre):
    imlec.execute(
        "CREATE TABLE IF NOT EXISTS kullanici_tb (kullanici_id INTEGER PRIMARY KEY  AUTOINCREMENT, eposta TEXT Unique,sifre)")
#    print(kitap_adi,kitap_yazari,okunma_durumu,begeni)
    kullanici_girisi = "INSERT INTO kullanici_tb (eposta,sifre) VALUES ('"+eposta+"','"+str(sifre)+"')"
    imlec.execute(kullanici_girisi)
    vt.commit()

def k_giris(eposta,sifre):
    try:
        imlec.execute("SELECT * FROM kullanici_tb where eposta='{}' and sifre='{}'".format(eposta,sifre))
        kullanici_id = imlec.fetchall()[0][0]
        return kullanici_id
    except:
        print("böyle bir kullanıcı yok")
        return 0
def ekle(k_id,kitap_adi="",kitap_yazari="",okunma_durumu="",begeni=""):
    imlec.execute(
        "CREATE TABLE IF NOT EXISTS kitaplik_tb (kitap_id INTEGER PRIMARY KEY  AUTOINCREMENT, kitap_adi,kitap_yazari,okunma_durumu,begeni, k_id INTEGER)")
#    print(kitap_adi,kitap_yazari,okunma_durumu,begeni)
    kitap_girisi = "INSERT INTO kitaplik_tb (kitap_adi,kitap_yazari,okunma_durumu,begeni, k_id) VALUES ('{}','{}','{}','{}','{}')".format(kitap_adi,kitap_yazari,okunma_durumu,begeni,k_id)
#    print(kitap_girisi)
    imlec.execute(kitap_girisi)
    vt.commit()
    return 1
def listele(k_id):
    imlec.execute("SELECT * FROM kitaplik_tb where k_id='{}'".format(k_id))
    kitaplar = imlec.fetchall()
    print(kitaplar)
    for i in kitaplar:
        for k in i:
            print(k, end=" ")
        print("")
    return kitaplar

def guncelle(guncellenecek):
    gkitap = input("Güncel kitap adını giriniz")
    gyazar = input("Güncel kitap yazarını")
    gokunma = input("Güncel kitap okunma durumunu giriniz")
    gbegeni = input("Güncel kitap beğeni değerini giriniz")
    guncelleme_kodu = "UPDATE kitaplik_tb SET kitap_adi='"+gkitap+"',kitap_yazari='"+gyazar+"',okunma_durumu='"+gokunma+"',begeni='"+gbegeni+"' WHERE kitap_id = '"+guncellenecek+"'"
    imlec.execute(guncelleme_kodu)
    vt.commit()
def sil(silinecek):
    silme_kodu="DELETE FROM kitaplik_tb WHERE kitap_id='"+silinecek+"'"
    imlec.execute(silme_kodu)
    vt.commit()
def cikis():
    vt.close()
    print("Çıkış Yapıldı İyi Günler")