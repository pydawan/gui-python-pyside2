# -*- coding: utf-8 -*-
"""Lendo arquivo de interface do tipo QWidget."""
from PySide2 import QtCore
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import (QApplication, QWidget)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        QUiLoader().load('./ui/MainWindow.xml', self)


if __name__ == "__main__":
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

    app = QApplication([])
    mainwindow = MainWindow()

    # icon = QIcon()
    # icon.addPixmap(QPixmap('../../assets/icons/icon.png'))
    # mainwindow.setWindowIcon(icon)

    mainwindow.show()
    sys.exit(app.exec_())
