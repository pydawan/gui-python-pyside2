# -*- coding: utf-8 -*-
"""
URLs:

- https://doc.qt.io/qt-5/qtquickcontrols2-universal.html
- https://doc.qt.io/qt-5/qtquickcontrols2-styles.html

- Default Style
- Fusion Style
- Imagine Style
- Material Style
- Universal Style

Variáveis de ambiente:

- QT_QUICK_CONTROLS_UNIVERSAL_THEME: Tema que será utilizado (Ex: 'Dark').
- QT_QUICK_CONTROLS_UNIVERSAL_ACCENT: Cor que será utilizada nos detalhes (Ex: 'Violet'.
- QT_QUICK_CONTROLS_UNIVERSAL_FOREGROUND: (Ex: 'Brown').
- QT_QUICK_CONTROLS_UNIVERSAL_BACKGROUND:

Constantes:

- Universal.Light: Light theme (default)
- Universal.Dark: Dark theme
- Universal.System: System theme
"""
import os

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

    os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Material'

    # sys.argv += ['--style', 'Default']
    # sys.argv += ['--style', 'Fusion']
    # sys.argv += ['--style', 'Imagine']
    # sys.argv += ['--style', 'Material']
    # sys.argv += ['--style', 'Universal']

    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon('../../assets/icons/icon.png'))

    engine = QQmlApplicationEngine()
    engine.load('./ui/interface-engine.qml')

    if not engine.rootObjects():
        sys.exit(-1)

    window = engine.rootObjects()[0]
    mainwindow = MainWindow(window=window)

    # Expondo o Python para o QML.
    # Caso os métodos sejam criados no QML (@SLOT()).
    context = engine.rootContext()
    context.setContextProperty('MainWindow', mainwindow)

    sys.exit(app.exec_())
