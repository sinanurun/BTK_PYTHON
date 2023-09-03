import sys
from kitapekle import KitapEkleEkrani
from anaekran_ui import Ui_AnaEkran
from PyQt5.QtWidgets import *

class Anaekran(QMainWindow,Ui_AnaEkran):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def kitap_ekle(self):
        print("kitap ekle tıklandı")
        # self.setCentralWidget(KitapEkleEkrani())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Anaekran()
    pencere.show()
    sys.exit(app.exec_())