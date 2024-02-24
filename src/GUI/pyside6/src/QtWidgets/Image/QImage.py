import sys, requests
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("pyside learn")


url = 'https://i.ytimg.com/vi/wOOq9OpQc1I/hq720.jpg'
r = requests.get(url)
print(r.content)
img = QImage('image.png')
img.loadFromData(r.content)

label = QLabel()
label.setPixmap(QPixmap.fromImage(img).scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))
# label.setPixmap(QPixmap.fromImage(img).scaled(80, 80, Qt.AspectRatioMode.IgnoreAspectRatio))

window.setCentralWidget(label)
window.show()
app.exec()