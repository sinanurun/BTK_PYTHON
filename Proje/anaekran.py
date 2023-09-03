import sys
from kitapekle import KitapEkleEkrani
from anaekran_ui import Ui_AnaEkran
from PyQt5.QtWidgets import *
import veritabani_06 as baglanti

class Anaekran(QMainWindow,Ui_AnaEkran):
    def __init__(self,k_id):
        super().__init__()
        self.k_id = k_id
        self.karsilama()
        self.kitap_listele()
    def karsilama(self):
        self.setupUi(self)
        self.actionKitapEkleme.triggered.connect(self.kitap_ekle)
        self.actionKitap_Listeleme.triggered.connect(self.kitap_listele)
        self.actionKitap_Silme.triggered.connect(self.kitap_silme)
        self.actionKitap_Guncelleme.triggered.connect(self.kitap_guncelle)

    def kitap_ekle(self):
        print("kitap ekle tıklandı")
        self.setCentralWidget(KitapEkleEkrani(self.k_id))
    def kitap_listele(self):
        self.karsilama()
        print("kitap liste tıklandı")
        kitaplar = baglanti.listele(self.k_id)
        satir_sayisi = len(kitaplar)
        print(satir_sayisi)
        self.tableWidget.setRowCount(satir_sayisi)
        k = 0
        print("hata durumu")
        for a in kitaplar:
            print("*",a)
            self.tableWidget.setItem(k, 0, QTableWidgetItem(str(a[0])))
            self.tableWidget.setItem(k, 1, QTableWidgetItem(str(a[1])))
            self.tableWidget.setItem(k, 2, QTableWidgetItem(str(a[2])))
            self.tableWidget.setItem(k, 3, QTableWidgetItem(str(a[3])))
            k += 1

    def kitap_silme(self):
        print("kitap silme tıklandı")
    def kitap_guncelle(self):
        print("kitap güncelle tıklandı")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Anaekran(1)
    pencere.show()
    sys.exit(app.exec_())