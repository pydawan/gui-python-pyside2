# -*- coding: utf-8 -*-
"""."""
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QAction


class MainWindow:
    def __init__(self, ui_file):
        self.label = ui_file.findChild(QLabel, 'label')

        self.line_edit = ui_file.findChild(QLineEdit, 'lineEdit')

        push_button = ui_file.findChild(QPushButton, 'pushButton')
        push_button.clicked.connect(self.change_label)

        action_sair = ui_file.findChild(QAction, 'actionSair')
        action_sair.triggered.connect(self.exit_app)

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

    ui_file = QUiLoader().load('./ui/MainWindow.ui')
    mainwindow = MainWindow(ui_file=ui_file)
    ui_file.show()

    sys.exit(app.exec_())
