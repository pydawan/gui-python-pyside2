# -*- coding: utf-8 -*-
"""."""
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        icon = QIcon()
        icon.addPixmap(QPixmap('../_icons/icon.png'))
        self.setWindowIcon(icon)

        # Título da janela.
        self.setWindowTitle('Título da janela')

        # Tamanho inicial da janela.
        self.resize(300, 300)

        # Tamanho mínimo da janela.
        self.setMinimumSize(100, 100)

        # Tamanho maximo da janela.
        self.setMaximumSize(500, 500)

        # Statusbar fica localizado na parte inferior da janela.
        self.statusBar().showMessage('Olá Mundo', 5000)


if __name__ == "__main__":
    import sys

    app = QApplication([])
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
