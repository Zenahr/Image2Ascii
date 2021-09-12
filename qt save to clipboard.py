import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QMainWindow):
    htmlFinished = pyqtSignal()
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.mHtml = ""
        self.view = QWebEngineView()
        self.setCentralWidget(self.view)
        self.view.setUrl(QUrl("http://www.google.com/"))
        file_menu = QMenu(self.menuBar())
        file_menu.setTitle("File")
        save_file_action = QAction(QIcon("disk--pencil.png"), "Save Page As...",self)
        file_menu.addAction(save_file_action)
        self.menuBar().addAction(file_menu.menuAction())
        save_file_action.triggered.connect(self.save_file)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Browser()
    w.show()
    cb = app.clipboard()
    cb.clear(mode=cb.Clipboard )
    cb.setText("Clipboard Text", mode=cb.Clipboard)
    sys.exit(app.exec_())