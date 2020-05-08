# -*- coding: utf-8 -*-
"""XML QMainWindow e connect.

Lendo arquivo de interface XML QMainWindow e utilizando o
`connect()` para executar um callback.
"""
from PySide2.QtCore import QObject, QCoreApplication, Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import (QApplication)


class MainWindow(QObject):
    def __init__(self):
        super().__init__()
        # Variável `window` **DEVE** utilizar `self`!
        # Variável window recebe a janela principal e os widgets.
        self.window = QUiLoader().load('./MainWindow.ui')

        # Acessando/atribuindo os widgets.
        self.label = self.window.findChild(QObject, 'label')
        self.line_edit = self.window.findChild(QObject, 'line_edit')

        push_button = self.window.findChild(QObject, 'push_button')
        # Conectando o signal a um slot.
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
