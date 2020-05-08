# -*- coding: utf-8 -*-
"""QQmlApplicationEngine.

Acessando um arquivo de interface (`QtQuick.Window`).
"""

from PySide2.QtCore import QObject
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQml import QQmlApplicationEngine


class MainWindow(QObject):
    def __init__(self):
        super().__init__()
        self.engine = QQmlApplicationEngine()
        self.engine.load('./MainWindow.qml')

        if not self.engine.rootObjects():
            sys.exit(-1)


if __name__ == "__main__":
    import sys

    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon('../../assets/icons/icon.png'))
    mainwindow = MainWindow()
    sys.exit(app.exec_())
