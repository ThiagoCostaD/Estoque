import sys
from Janelas.janelaSenha import *
from PyQt5.QtWidgets import QMainWindow, QApplication


class Tabela(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

    def tabela(self):
        pass


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tabela = Tabela()
    tabela.show()
