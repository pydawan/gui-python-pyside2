# -*- coding: utf-8 -*-
"""."""
from PySide2.QtCore import QObject, QSize, QUrl
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQuick import QQuickView


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


if __name__ == '__main__':
    import sys

    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon('../../_icons/icon.png'))

    view = QQuickView()
    view.setTitle('Python PySide2 e QQuickView()')
    view.resize(800, 600)
    view.setMinimumSize(QSize(400, 300))
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setSource(QUrl.fromLocalFile('./ui/interface_qquickview.qml'))

    if view.status() == QQuickView.Error:
        sys.exit(-1)

    ui = MainWindow(win=view)
    view.show()
    sys.exit(app.exec_())
