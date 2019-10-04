# -*- coding: utf-8 -*-
"""."""
from PySide2.QtCore import QObject
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQml import QQmlApplicationEngine


class MainWindow:
    def __init__(self, win):

        self.labe1 = win.findChild(QObject, 'label')
        self.text_field = win.findChild(QObject, 'textfield')
        self.button = win.findChild(QObject, 'button')
        self.button.clicked.connect(self.change_label)

    def change_label(self):
        if self.text_field.property('text'):
            self.labe1.setProperty('text', self.text_field.property('text'))
        else:
            self.labe1.setProperty('text', 'Digite algo no campo de texto :)')


if __name__ == "__main__":
    import sys

    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon('icons/icon.png'))
    engine = QQmlApplicationEngine()
    engine.load('./ui/MainWindow.qml')
    if not engine.rootObjects():
        sys.exit(-1)
    win = engine.rootObjects()[0]
    ui = MainWindow(win=win)
    sys.exit(app.exec_())
