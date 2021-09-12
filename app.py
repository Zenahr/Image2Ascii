from threading import Thread
import sys
from flask import Flask, render_template
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
from time import sleep

webInstance = Flask(__name__)
# webInstance.config['PORT'] = 5000

@webInstance.route('/')
def index():
    return render_template('index.html')

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.setWindowTitle("Application Title")
        self.browser.setUrl(QUrl("http://127.0.0.1:5000"))
        self.setCentralWidget(self.browser)
        self.show()

webInstanceConfig = {'host': '127.0.0.1', 'port': 5000, 'threaded': True, 'use_reloader': False, 'debug': True}
Thread(target=webInstance.run, daemon=True, kwargs=webInstanceConfig).start()
# sleep(2)
app = QApplication(sys.argv)
window = MainWindow()
app.exec_()