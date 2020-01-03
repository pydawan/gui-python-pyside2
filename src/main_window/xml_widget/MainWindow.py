# -*- coding: utf-8 -*-
"""Lendo arquivo de interface do tipo QWidget."""
from PySide2 import QtCore
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton, QWidget)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        QUiLoader().load('./forms/MainWindow.ui', self)

        self.label = self.findChild(QLabel, 'label')

        self.line_edit = self.findChild(QLineEdit, 'lineEdit')

        push_button = self.findChild(QPushButton, 'pushButton')
        push_button.clicked.connect(self.change_label)

    def change_label(self):
        text = self.line_edit.text()
        if text:
            self.label.setText(text)
        else:
            self.label.setText('Digite algo no campo de texto :)')


if __name__ == "__main__":
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

    app = QApplication([])
    mainwindow = MainWindow()

    icon = QIcon()
    icon.addPixmap(QPixmap('../../_icons/icon.png'))
    mainwindow.setWindowIcon(icon)

    mainwindow.show()
    sys.exit(app.exec_())
