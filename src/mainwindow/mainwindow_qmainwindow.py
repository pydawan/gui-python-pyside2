# -*- coding: utf-8 -*-
"""Configurando a janela principal (QMainWindow)."""
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    """Classe MainWindow herda de QMainWindow().

    `QMainWindow()` possui:

    - Barra de menu ``menuBar()``.
    - Barra de status ``statusBar()``.
    - Barra de ferramentas ``addToolBar()``.
    """

    def __init__(self):
        super().__init__()
        pass


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

    # Título da janela.
    mainwindow.setWindowTitle('Título da janela')

    # Ícone da janela principal
    icon = QIcon()
    icon.addPixmap(QPixmap('../assets/icons/icon.png'))
    mainwindow.setWindowIcon(icon)

    mainwindow.show()
    sys.exit(app.exec_())
