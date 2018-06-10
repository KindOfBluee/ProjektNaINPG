import os,sys
from subprocess import Popen
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.tet = QtWidgets.QPushButton('Tetris')
        self.pong = QtWidgets.QPushButton('Pong')
        self.snake = QtWidgets.QPushButton('Snake')
        self.ttt = QtWidgets.QPushButton('Tic-Tac-Toe')

        self.logo = QtWidgets.QLabel('Miejsce na LOGO')
        self.logo.setAlignment(QtCore.Qt.AlignCenter)

        self.obraz = QtWidgets.QLabel(self)
        self.obraz.setPixmap(QPixmap('tetris.png'))
        self.obraz.setAlignment(QtCore.Qt.AlignCenter)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.logo)

        button_box = QtWidgets.QVBoxLayout()
        button_box.addWidget(self.tet)
        button_box.addWidget(self.pong)
        button_box.addWidget(self.snake)
        button_box.addWidget(self.ttt)

        horizontal_box = QtWidgets.QHBoxLayout()
        horizontal_box.addLayout(button_box)
        horizontal_box.addWidget(self.obraz)

        vertical_box = QtWidgets.QVBoxLayout()
        vertical_box.addLayout(h_box)
        vertical_box.addLayout(horizontal_box)

        self.setLayout(vertical_box)
        self.setWindowTitle('Main Menu')

        self.tet.clicked.connect(self.btn_tetris)
        self.pong.clicked.connect(self.btn_pong)
        self.setGeometry(300,300,800,600)
        self.show()

    def btn_tetris(self):
        os.system("cd tetris && python pytetris.py")

    def btn_pong(self):
        os.system("cd Pong && python pong.py")


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())