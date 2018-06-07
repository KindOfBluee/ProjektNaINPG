import sys
from PyQt5 import QtWidgets

print("halo")


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.show()
    sys.exit(app.exec_())


window()
