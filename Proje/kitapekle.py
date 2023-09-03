from kitapekle_ui import Ui_KitapEkleForm
from PyQt5.QtWidgets import *
import sys
import veritabani_06 as baglanti
class KitapEkleEkrani(QWidget, Ui_KitapEkleForm):
    def __init__(self,k_id):
        super().__init__()
        self.k_id = k_id
        self.setupUi(self)
        self.kitapKayitButton.clicked.connect(self.kitap_ekle)

    def kitap_ekle(self):
        k_adi = self.kitapAdiLineEdit.text()
        k_yazari = self.kitapYazariLineEdit.text()
        k_durum = self.okunmaDurumuCheckBox.checkState()
        k_begeni = self.beEniDurumuComboBox.currentText()
        sonuc = baglanti.ekle(self.k_id,k_adi,k_yazari,k_durum,k_begeni)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = KitapEkleEkrani(1)
    pencere.show()
    sys.exit(app.exec_())