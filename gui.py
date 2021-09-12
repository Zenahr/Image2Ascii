from threading import Thread
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import * # requires pip install PyQtWebEngine
import sys
from time import sleep
import subprocess

def startDjangoServer():
    subprocess.Popen('server\\server.exe runserver 127.0.0.1:8000 --noreload', shell=True)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.setWindowTitle("IMAGE2ASCII")
        self.browser.setUrl(QUrl("http://127.0.0.1:8000"))
        self.setCentralWidget(self.browser)
        self.show()

startDjangoServer()
app = QApplication(sys.argv)
window = MainWindow()
app.exec_()