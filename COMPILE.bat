pyinstaller --name=server manage.py --log-level CRITICAL --hidden-import=app/settings.py --hidden-import=staff --hidden-import=staff.apps --hidden-import=app.apps --hidden-import=staff.urls --hidden-import=staff.forms --hidden-import=staff.middleware --hidden-import=staff.tests --hidden-import=staff.urls --hidden-import=staff.views --hidden-import=app.middleware -y
xcopy _images dist\server\_images\ /E/H
xcopy app\static\ dist\server\static\ /E/H
pyinstaller --name=Image2Ascii gui.py --log-level CRITICAL --onefile --noconsole -y
RUN_EXE.bat