from . import cadastroUsuario, senha, tabela
import sys
from PyQt5.QtWidgets import QMainWindow


class App(cadastroUsuario, senha, tabela, QMainWindow):
    def __init__(self, parent: None):
        super().__init__(parent)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
