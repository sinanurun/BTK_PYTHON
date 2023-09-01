import sqlite3 as sql

vt = sql.connect('kitaplik.sqlite')
imlec = vt.cursor()
try:
    imlec.execute('CREATE TABLE IF NOT EXISTS kitap_bilgisi (kitap_adi,kitap_yazari, okunma_durumu,begeni)')
except:
    print("tablo zaten vardı oluşturmadı")

kitap_girisi = "INSERT INTO kitap_bilgisi VALUES ('Suç ve Ceza', 'Dostoyevski', 'hayır','*****')"

imlec.execute(kitap_girisi)
imlec.execute("INSERT INTO kitap_bilgisi VALUES ('Beyaz Diş', 'Jack LONDON', 'evet','***')")

imlec.execute("INSERT INTO kitap_bilgisi VALUES ('Yunan Mitolojisi', 'Anna', 'hayır','****')")
vt.commit()

vt.close()
