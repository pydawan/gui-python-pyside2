
URLs:

- https://doc.qt.io/qt-5/qtquickcontrols2-universal.html
- https://doc.qt.io/qt-5/qtquickcontrols2-styles.html

## QML

## Variáveis de ambiente

- QT_QUICK_CONTROLS_UNIVERSAL_THEME: Tema que será utilizado (Ex: 'Dark').
- QT_QUICK_CONTROLS_UNIVERSAL_ACCENT: Cor que será utilizada nos detalhes (Ex: 'Violet').
- QT_QUICK_CONTROLS_UNIVERSAL_FOREGROUND: (Ex: 'Brown').
- QT_QUICK_CONTROLS_UNIVERSAL_BACKGROUND: (Ex: 'Steel').

Exemplo:

```python
os.environ['QT_QUICK_CONTROLS_UNIVERSAL_THEME'] = 'Dark'
os.environ['QT_QUICK_CONTROLS_UNIVERSAL_ACCENT'] = 'Violet'
os.environ['QT_QUICK_CONTROLS_UNIVERSAL_FOREGROUND'] = 'Brown'
os.environ['QT_QUICK_CONTROLS_UNIVERSAL_BACKGROUND'] = 'Steel'
```

## Cores pré definidas

- Universal.Lime: #A4C400
- Universal.Green: #60A917
- Universal.Emerald: #008A00
- Universal.Teal: #00ABA9
- Universal.Cyan: #1BA1E2
- Universal.Cobalt: #3E65FF (default accent)
- Universal.Indigo: #6A00FF
- Universal.Violet: #AA00FF
- Universal.Pink: #F472D0
- Universal.Magenta: #D80073
- Universal.Crimson: #A20025
- Universal.Red: #E51400
- Universal.Orange: #FA6800
- Universal.Amber: #F0A30A
- Universal.Yellow: #E3C800
- Universal.Brown: #825A2C
- Universal.Olive: #6D8764
- Universal.Steel: #647687
- Universal.Mauve: #76608A
- Universal.Taupe: #87794E 

## Constantes:

- Universal.Light: Light theme (default)
- Universal.Dark: Dark theme
- Universal.System: System theme

Como definir o estilo:
```python
os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Default'
os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Fusion'
os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Imagine'
os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Material'
os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Universal'
os.environ['QT_QUICK_CONTROLS_STYLE'] = 'org.kde.desktop'
```

- Default Style
- Fusion Style
- Imagine Style
- Material Style
- Universal Style

```python
sys.argv += ['--style', 'Default']
sys.argv += ['--style', 'Fusion']
sys.argv += ['--style', 'Imagine']
sys.argv += ['--style', 'Material']
sys.argv += ['--style', 'Universal']
sys.argv += ['--style', 'org.kde.desktop']
```

# Como instalar o kirigami2

## Fedora

```bash
sudo dnf install kf5-kirigami2 kf5-kirigami2-devel
```

## Ubuntu

```bash
sudo apt install kirigami2 kirigami2-dev
```

   



