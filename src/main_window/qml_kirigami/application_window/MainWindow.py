# -*- coding: utf-8 -*-
"""
sudo apt install qml-module-org-kde-kirigami2
org.kde.kirigami
"""
from PySide2.QtCore import QObject, Slot
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQml import QQmlApplicationEngine


class MainWindow(QObject):
    def __init__(self, window):
        super().__init__()

        self.labe1 = window.findChild(QObject, 'label')
        self.text_field = window.findChild(QObject, 'textfield')
        button = window.findChild(QObject, 'button')
        button.clicked.connect(self.change_label)

    def change_label(self):
        if self.text_field.property('text'):
            self.labe1.setProperty('text', self.text_field.property('text'))
        else:
            self.labe1.setProperty('text', 'Digite algo no campo de texto :)')

    @Slot(str)
    def _on_button_clicked(self, text):
        print('Botão clicado (Python)')
        if text:
            self.labe1.setProperty('text', text)
        else:
            self.labe1.setProperty('text', 'Digite algo no campo de texto :)')


if __name__ == "__main__":
    import sys

    # os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Material'
    # os.environ['QT_QUICK_CONTROLS_STYLE'] = 'org.kde.desktop'

    # sys.argv += ['--style', 'Default']
    # sys.argv += ['--style', 'Fusion']
    # sys.argv += ['--style', 'Imagine']
    # sys.argv += ['--style', 'Material']
    # sys.argv += ['--style', 'Universal']

    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon('../../_icons/icon.png'))

    engine = QQmlApplicationEngine()
    engine.load('./ui/MainWindow.qml')

    if not engine.rootObjects():
        sys.exit(-1)

    window = engine.rootObjects()[0]
    mainwindow = MainWindow(window=window)

    # Expondo o Python para o QML.
    # Caso os métodos sejam criados no QML (@SLOT()).
    context = engine.rootContext()
    context.setContextProperty('MainWindow', mainwindow)

    sys.exit(app.exec_())
