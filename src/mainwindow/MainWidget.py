# -*- coding: utf-8 -*-
"""QWidget.

Criando uma aplicativo do tipo QWidget com Python e utilizando o
`connect()` para executar um callback.
"""
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QWidget


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        screen_size = app.primaryScreen().geometry()
        width = screen_size.width()
        height = screen_size.height()

        # Tamanho inicial da janela.
        self.resize(int(width / 2), int(height / 2))
        # Tamanho mínimo da janela.
        self.setMinimumSize(int(width / 2), int(height / 2))
        # Tamanho maximo da janela.
        self.setMaximumSize(width - 200, height - 200)

        # Título da janela.
        self.setWindowTitle('Título da janela')

        # Ícone da janela principal
        icon = QIcon()
        icon.addPixmap(QPixmap('../assets/icons/icon.png'))
        self.setWindowIcon(icon)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainwidget = MainWidget()
    mainwidget.show()
    sys.exit(app.exec_())
