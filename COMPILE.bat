pyinstaller --name=Image2Ascii manage.py --log-level CRITICAL -y --hidden-import=app/settings.py --hidden-import=staff --hidden-import=staff.apps --hidden-import=app.apps --hidden-import=staff.urls --hidden-import=staff.forms --hidden-import=staff.middleware --hidden-import=staff.tests --hidden-import=staff.urls --hidden-import=staff.views --hidden-import=app.middleware
xcopy _images dist\Image2Ascii\_images\ /E/H
xcopy app\static\ dist\Image2Ascii\static /E/H
RUN_EXE.bat


