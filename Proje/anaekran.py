import sys
from kitapekle import KitapEkleEkrani
from anaekran_ui import Ui_AnaEkran
from PyQt5.QtWidgets import *

class Anaekran(QMainWindow,Ui_AnaEkran):
    def __init__(self):
        super(Anaekran,self).__init__()
        self.karsilama()
    def karsilama(self):
        self.setupUi(self)
        self.actionKitapEkleme.triggered.connect(self.kitap_ekle)
        self.actionKitap_Listeleme.triggered.connect(self.kitap_listele)
        self.actionKitap_Silme.triggered.connect(self.kitap_silme)
        self.actionKitap_Guncelleme.triggered.connect(self.kitap_guncelle)
    def kitap_ekle(self):
        print("kitap ekle tıklandı")
        self.setCentralWidget(KitapEkleEkrani())
    def kitap_listele(self):
        print("kitap liste tıklandı")
        self.karsilama()
    def kitap_silme(self):
        print("kitap silme tıklandı")
    def kitap_guncelle(self):
        print("kitap güncelle tıklandı")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Anaekran()
    pencere.show()
    sys.exit(app.exec_())