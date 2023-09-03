import sys
from PyQt5.QtWidgets import *
from anaekran_ui import Ui_Anaekran

class AnaekranPenceresi(QWidget,Ui_Anaekran):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.A_Button.clicked.connect(self.arttir)
        self.buton2.clicked.connect(self.arttir2)
    def arttir(self):
        self.C_Label.setText("Birinci Buton")
    def arttir2(self):
        self.C_Label.setText("İkinci Buton")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AnaekranPenceresi()
    pencere.show()
    sys.exit(app.exec_())