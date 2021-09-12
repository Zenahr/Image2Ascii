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
        # self.setStyleSheet('''
        #     QMenu {
        #         background: lightBlue;
        #         color: orange;
        #     }
        #     QMenu::item:selected {
        #         background: lightGray;
        #     }
        # '''
        # )
        self.browser = QWebEngineView()
        self.setWindowTitle("IMAGE2ASCII")
        self.browser.setUrl(QUrl("http://127.0.0.1:8000"))
        self.setCentralWidget(self.browser)
        file_menu = QMenu(self.menuBar())
        file_menu.setTitle("File")
        save_file_action = QAction(QIcon("disk--pencil.png"), "Save Page As...",self)
        file_menu.addAction(save_file_action)
        self.menuBar().addAction(file_menu.menuAction())
        save_file_action.triggered.connect(self.save_file)
        self.show()

    def contextMenuEvent(self, event):
        self.menu = self.page().createStandardContextMenu()
        self.menu.addAction('My action')
        self.menu.popup(event.globalPos())

    def callback(self, html):
        self.mHtml = html
        self.htmlFinished.emit()

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "", "Hypertext Markup Language (*.htm *.html);;" "All files(*.*)")
        if filename:
            self.view.page().toHtml(self.callback)
            loop = QEventLoop()
            self.htmlFinished.connect(loop.quit)
            loop.exec_()
            with open(filename, 'w') as f:
                f.write(self.mHtml)

startDjangoServer()
# app = QApplication(sys.argv)
# window = MainWindow()
# app.exec_()

import native_web_app
url = "http://127.0.0.1:8000"
try:
    native_web_app.open(url)
except Exception:
    print(f"No web browser found. Please open a browser and point it to {url}.")