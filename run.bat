 cd %~dp0
set CUR_DIR=%~dp0
set VENV=%CUR_DIR%\venv\Scripts\activate.bat
set PYTHON=%CUR_DIR%\venv\Scripts\python.exe
set RunScript=%CUR_DIR%crawler.py


cmd /c %PYTHON% %RunScript%