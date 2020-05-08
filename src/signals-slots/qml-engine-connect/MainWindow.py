# -*- coding: utf-8 -*-
"""QQmlApplicationEngine.

Acessando um arquivo de interface (`QtQuick.Window`) e utilizando o
`connect()` para executar uma ação (callback).
"""
from PySide2.QtCore import QObject
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQml import QQmlApplicationEngine


class MainWindow(QObject):

    def __init__(self):
        super().__init__()
        # Lendo o arquivo de interface.
        self.engine = QQmlApplicationEngine()
        self.engine.load('./MainWindow.qml')
        if not self.engine.rootObjects():
            sys.exit(-1)

        # Acessando os a janela principal e os widgets.
        self.window = self.engine.rootObjects()[0]
        self.label = self.window.findChild(QObject, 'label')
        self.text_field = self.window.findChild(QObject, 'text_field')

        button = self.window.findChild(QObject, 'button')
        # Conectando o sinal de clique a um método (callback).
        button.clicked.connect(self.change_label)

    def change_label(self):
        if self.text_field.property('text'):
            self.label.setProperty('text', self.text_field.property('text'))
        else:
            self.label.setProperty('text', 'Digite algo no campo de texto :)')


if __name__ == "__main__":
    import sys

    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon('../../assets/icons/icon.png'))
    mainwindow = MainWindow()
    sys.exit(app.exec_())
