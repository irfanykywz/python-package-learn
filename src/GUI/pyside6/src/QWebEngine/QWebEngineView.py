import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("pyside learn")

web = QWebEngineView()
# web.load('https://google.com')
web.setHtml('<h1>hello world</h1>')


window.setCentralWidget(web)
window.show()
app.exec()