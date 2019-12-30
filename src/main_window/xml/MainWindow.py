# -*- coding: utf-8 -*-
"""."""
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton, QAction, QMainWindow)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        window = QUiLoader().load('./forms/MainWindow.ui', self)

        self.label = self.findChild(QLabel, 'label')

        self.line_edit = self.findChild(QLineEdit, 'lineEdit')

        push_button = self.findChild(QPushButton, 'pushButton')
        push_button.clicked.connect(self.change_label)

        action_sair = self.findChild(QAction, 'actionSair')
        action_sair.triggered.connect(self.exit_app)

        window.show()

    def exit_app(self):
        QApplication.quit()

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
    sys.exit(app.exec_())
