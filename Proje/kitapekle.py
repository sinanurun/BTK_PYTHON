from kitapekle_ui import Ui_KitapEkleForm
from PyQt5.QtWidgets import *
import sys

class KitapEkleEkrani(QWidget, Ui_KitapEkleForm):
    def __init__(self):
        super(KitapEkleEkrani,self).__init__()
        self.fbaslat()
    def fbaslat(self):
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = KitapEkleEkrani()
    pencere.show()
    sys.exit(app.exec_())