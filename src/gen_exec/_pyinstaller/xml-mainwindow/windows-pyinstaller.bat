pyinstaller --noconfirm --log-level=WARN ^
--windowed ^
--name="Exemplo" ^
--add-data="icons\;icons" ^
--add-data="ui\;ui" ^
--paths="C:\Windows\System32\downlevel" ^
--paths="%~dp0\dlls" ^
--icon=icons\icon.ico ^
mainwindow.py