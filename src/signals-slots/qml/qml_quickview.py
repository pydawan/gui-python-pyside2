# -*- coding: utf-8 -*-
"""."""
from PySide2.QtCore import QObject, QSize, QUrl
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQuick import QQuickView


class MainWindow(QQuickView):
    def __init__(self):
        super().__init__()
        self.setTitle('Python PySide2 e QQuickView()')
        self.resize(800, 600)
        self.setMinimumSize(QSize(400, 300))
        self.setResizeMode(QQuickView.SizeRootObjectToView)
        self.setSource(QUrl.fromLocalFile('./ui/interface-qquickview.qml'))

        if self.status() == QQuickView.Error:
            sys.exit(-1)

        self.labe1 = self.findChild(QObject, 'label')
        self.text_field = self.findChild(QObject, 'textfield')
        self.button = self.findChild(QObject, 'button')
        self.button.clicked.connect(self.change_label)

        self.show()
        # del self

    def change_label(self):
        if self.text_field.property('text'):
            self.labe1.setProperty('text', self.text_field.property('text'))
        else:
            self.labe1.setProperty('text', 'Digite algo no campo de texto :)')


if __name__ == '__main__':
    import sys

    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon('../../assets/icons/icon.png'))

    mainwindow = MainWindow()

    app.exec_()
