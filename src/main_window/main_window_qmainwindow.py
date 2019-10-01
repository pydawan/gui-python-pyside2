# -*- coding: utf-8 -*-
"""Configurando a janela principal (QMainWindow)."""
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self, screen_size):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('Título da janela')

        # Ícone da janela principal
        icon = QIcon()
        icon.addPixmap(QPixmap('../_icons/icon.png'))
        self.setWindowIcon(icon)

        # Tamanho inicial da janela.
        width = screen_size.width()
        height = screen_size.height()
        self.resize(width / 2, height / 2)

        # Tamanho mínimo da janela.
        self.setMinimumSize(width / 2, height / 2)

        # Tamanho maximo da janela.
        self.setMaximumSize(width - 200, height - 200)


if __name__ == "__main__":
    import sys

    app = QApplication([])

    screen_size = app.desktop().geometry()
    # screen_size = app.primaryScreen().geometry()

    mainwindow = MainWindow(screen_size=screen_size)
    mainwindow.show()
    sys.exit(app.exec_())
