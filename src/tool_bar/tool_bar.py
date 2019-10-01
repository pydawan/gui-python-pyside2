# -*- coding: utf-8 -*-
"""."""
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QToolBar


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

        # Toolbar pode ser movido para diversas áreas da janela.
        tool_bar = QToolBar()
        tool_bar.setToolTip('Barra de ferramentas')
        self.addToolBar(tool_bar)

        icon_copy = QIcon('../_icons/copy-64x64.png')
        tool_bar.addAction(icon_copy, 'Copiar', self.action_copy).setToolTip('Copiar')

        icon_paste = QIcon('../_icons/paste-64x64.png')
        tool_bar.addAction(icon_paste, 'Colar', self.action_paste).setToolTip('Colar')

    @staticmethod
    def action_copy():
        print('Copiar')

    @staticmethod
    def action_paste():
        print('Colar')


if __name__ == "__main__":
    import sys

    app = QApplication([])
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
