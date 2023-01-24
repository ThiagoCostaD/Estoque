import sys
from Janelas.novoUsuario import *
from PyQt5.QtWidgets import QMainWindow, QApplication


class Tabela(QMainWindow, Ui_Cadastro):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

    def tabela(self):
        pass


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tabela = Tabela()
    tabela.show()
    qt.exec_()
