# -*- coding: utf-8 -*-
"""Configurando a janela principal (QWiget)."""
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    """MainWndow herda de QWidget().

    `QWidget()` é o tipo mais simples de janela, sendo assim ela não
    possui barra de status ou mesmo menus.
    """
    def __init__(self):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('Título da janela')

        # Ícone da janela principal
        icon = QIcon()
        icon.addPixmap(QPixmap('../assets/icons/icon.png'))
        self.setWindowIcon(icon)


if __name__ == "__main__":
    import sys

    app = QApplication([])

    screen_size = app.desktop().geometry()
    # screen_size = app.primaryScreen().geometry()

    width = screen_size.width()
    height = screen_size.height()

    mainwindow = MainWindow()
    # Tamanho inicial da janela.
    mainwindow.resize(width / 2, height / 2)
    # Tamanho mínimo da janela.
    mainwindow.setMinimumSize(width / 2, height / 2)
    # Tamanho maximo da janela.
    mainwindow.setMaximumSize(width - 200, height - 200)
    mainwindow.show()
    sys.exit(app.exec_())
