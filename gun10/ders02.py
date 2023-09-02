import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


class p_sinifi(QWidget):
    def __init__(self):
        super().__init__()
        self.ekran_tasarla()
        self.tiklanmasayisi = 0

    def ekran_tasarla(self):
        QToolTip.setFont(QFont('verdana', 22))
        self.setToolTip("bu bir penceredir")
        self.buton_01 = QPushButton("Düğme", self)
        self.buton_01.clicked.connect(self.tiklandi)
        self.buton_01.move(100, 100)
        self.buton_01.setGeometry(50, 50, 100, 100)
        self.buton_01.setToolTip("bu tıklanabilir bir butondur")
        self.setGeometry(150, 250, 500, 300)
        self.setWindowTitle("Buton Uygulaması")
        self.label = QLabel("0",self)
        self.label.setGeometry(250,250,50,50)
        self.show()
    def tiklandi(self):
        print("butona tıklandı")
        self.buton_01.setText("Tıklandı")
        self.tiklanmasayisi += 1
        self.label.setText(str(self.tiklanmasayisi))



if __name__ == '__main__':
    uygulama = QApplication(sys.argv)
    pencere = p_sinifi()
    sys.exit(uygulama.exec())
