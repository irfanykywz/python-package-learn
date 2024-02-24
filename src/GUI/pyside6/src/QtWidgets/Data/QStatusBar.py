import sys
from PySide6.QtWidgets import QApplication, QWidget, QStatusBar, QPushButton, QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyside learn")

def set_status():
    status.showMessage('heheboi')

button = QPushButton('Submit')
button.clicked.connect(set_status)

status = QStatusBar()
# status.setSizeGripEnabled(False) # remove resize grip


layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(status)

window.setLayout(layout)
window.show()
app.exec()