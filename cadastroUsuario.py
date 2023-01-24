import sys
from Janelas.novoUsuario import *
from PyQt5.QtWidgets import QMainWindow, QApplication


class CadastroUsuario(QMainWindow, Ui_Cadastro):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

    def usuario(self):
        pass


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    cadastro = CadastroUsuario()
    cadastro.show()
    qt.exec_()
