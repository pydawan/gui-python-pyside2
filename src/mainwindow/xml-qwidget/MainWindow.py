# -*- coding: utf-8 -*-
"""QWidget.

Lendo arquivo de interface QWidget.
"""
from PySide2.QtCore import QObject, QCoreApplication, Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication


class MainWindow(QObject):
    def __init__(self):
        super().__init__()
        # Variável DEVE ter o self!
        self.window = QUiLoader().load('./MainWindow.ui')
        self.window.show()


if __name__ == "__main__":
    import sys

    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec_())
