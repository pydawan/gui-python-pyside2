# -*- coding: utf-8 -*-
"""Janela do tipo ``QMainWindow()``."""
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
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
