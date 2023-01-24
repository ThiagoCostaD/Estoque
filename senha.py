import sys
from Janelas.janelaSenha import *
from PyQt5.QtWidgets import QMainWindow, QApplication


class SenhaMestre(QMainWindow, Ui_Acesso):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

    def senha(self, usuario, senha):
        pass


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    senha = SenhaMestre()
    senha.show()
    qt.exec_()
