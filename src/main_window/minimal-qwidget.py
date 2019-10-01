# -*- coding: utf-8 -*-
"""Janela do tipo ``QWidget()``."""
from PySide2.QtWidgets import QWidget, QApplication


class MainWindow(QWidget):
    """MainWndow herda de QWidget().

    `QWidget()` é o tipo mais simples de janela, sendo assim ela não
    possui barra de status ou mesmo menus.
    """

    def __init__(self):
        super().__init__()
        pass


if __name__ == "__main__":
    import sys

    app = QApplication([])
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
