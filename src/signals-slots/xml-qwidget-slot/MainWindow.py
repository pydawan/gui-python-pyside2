# -*- coding: utf-8 -*-
"""QWidget.

Lendo arquivo de interface do tipo QWidget e utilizando o connect()
para executar um callback.

Ainda não funciona!
"""
from PySide2.QtCore import QObject, QCoreApplication, Qt, Slot
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import (QApplication, QLabel, QLineEdit)


class MainWindow(QObject):
    def __init__(self):
        super().__init__()
        self.window = QUiLoader().load('./MainWindow.xml')
        self.label = self.window.findChild(QLabel, 'label')
        self.line_edit = self.window.findChild(QLineEdit, 'line_edit')

        self.window.show()

    @Slot()
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
