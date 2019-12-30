- [Instalar o Qt Creator](./docs/install-qt-creator.md).
- [Instalar o Qt Designer](./docs/install-qt-designer.md).

# PySide2


## Instalação

É recomenda a instalação dentro de uma ambiente virtual (pyenv, pipenv, virtualenv, etc)

```bash
pip install PySide2
```

## MainWindow

- [Código minimo para criar janela com QWidget](./src/main_window/minimal-qwidget.py).
- [Configurando janela do tipo QWidget](./src/main_window/main_window_qwidget.py).
- [Código minimo para criar janela com QMainWindow](./src/main_window/minimal-qmainwindow.py).
- [Configurando janela do tipo QMainWindow](./src/main_window/main_window_qmainwindow.py).

---

- [Barra de menus](./src/menu_bar/menu_bar.py)
- [Barra de status](./src/status_bar/status_bar.py)
- [Barra de ferramentas](./src/tool_bar/tool_bar.py)

## Abrindo arquivos QML

- [lendo arquivos qml engine](./src/main_window/qml/qml_engine.py).
- [lendo arquivos qml quickview](./src/main_window/qml/qml_quickview.py).

## Abrindo arquivos XML

- [lendo arquivos XML](./src/main_window/xml/MainWindow.py)

## Layouts

- [QHBoxLayout](./src/layouts/qhboxlayout.py) Layout posiciona os widgets horizontalmente (linha).
- [QVBoxLayout](./src/layouts/qvboxlayout.py) Layout posiciona os widgets verticalmente (coluna).
- [QGridLayout](./src/layouts/qgridlayout.py) Layout posiciona os widgets em celulas (linhas e colunas).
- [QFormLayout](./src/layouts/qformlayout.py) Layout posiciona os widgets como em um formulario (varias linhas 2 colunas).

## Kirigami

sudo apt install qml-module-org-kde-kirigami2

Atualmente está com o bug **module "org.kde.kirigami" is not installed**: https://www.mail-archive.com/debian-qt-kde@lists.debian.org/msg89572.html

## Banco de dados

Exemplos de CRUD sem utilizar model:

- [SQLite3](./src/database/db-sqlite/ConnectSQLite.py)
- [PostgreSQL](./src/database/db-postgres/ConnectPostgreSQL.py)
