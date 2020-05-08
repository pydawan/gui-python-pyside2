# -*- coding: utf-8 -*-
"""QWidget.

Lendo arquivo de interface do tipo QWidget e utilizando o connect()
para executar um callback.
"""
from PySide2.QtCore import QObject, QCoreApplication, Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton)


class MainWindow(QObject):
    def __init__(self):
        super().__init__()
        self.window = QUiLoader().load('./MainWindow.ui')
        self.label = self.window.findChild(QLabel, 'label')
        self.line_edit = self.window.findChild(QLineEdit, 'line_edit')

        push_button = self.window.findChild(QPushButton, 'push_button')
        push_button.clicked.connect(self.on_button_clicked)

        self.window.show()

    def on_button_clicked(self):
        text = self.line_edit.text()
        if text:
            self.label.setText(text)
        else:
            self.label.setText('Digite algo no campo de texto :)')


if __name__ == "__main__":
    import sys

    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec_())
