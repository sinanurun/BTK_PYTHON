import sys
from PyQt5 import QtWidgets

uygulama = QtWidgets.QApplication(sys.argv)

pencere = QtWidgets.QWidget()

pencere.setWindowTitle("BTK Python Kursu")

pencere.show()

sys.exit(uygulama.exec())