import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Main Menu'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Pliki')
        editMenu = mainMenu.addMenu('Edytuj')
        viewMenu = mainMenu.addMenu('Widok')
        searchMenu = mainMenu.addMenu('Wyszukaj')
        toolsMenu = mainMenu.addMenu('Narzedzia')
        helpMenu = mainMenu.addMenu('Pomoc')

        exitButton = QAction(QIcon('exit24.png'), 'Wyjscia', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Wyjscie z aplikacji')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())