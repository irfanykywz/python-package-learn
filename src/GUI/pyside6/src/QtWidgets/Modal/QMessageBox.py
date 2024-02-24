# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

def buttonAct():
    m = QMessageBox()
    m.setMinimumSize(300,200)
    m.setWindowTitle('Alat untuk jadi anime')
    m.setText('kamu berhasil menjadi anime ?')
    m.setInformativeText('****************')
    # m.setIcon(QMessageBox.Critical)
    # m.setIcon(QMessageBox.Question)
    m.setIcon(QMessageBox.Information)
    # m.setIcon(QMessageBox.Warning)
    m.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    m.setDefaultButton(QMessageBox.Ok)
    ret = m.exec()
    if ret == QMessageBox.Ok:
        print('ok')
    else:
        print('cancel')



app = QApplication(sys.argv)
window = QWidget()

button = QPushButton("Show message")
button.clicked.connect(buttonAct)

button2 = QPushButton('Show message lambda')
button2.clicked.connect(lambda : QMessageBox.warning(window, 'Hello', 'this is message box'))

button3 = QPushButton('Custom Button')
button3.clicked.connect(lambda : QMessageBox.warning(window, "My Application",
        "The document has been modified.\n"
           "Do you want to save your changes?",
        QMessageBox.Save | QMessageBox.Discard
        | QMessageBox.Cancel,
        QMessageBox.Save))

layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(button2)
layout.addWidget(button3)
window.setLayout(layout)


window.show()
app.exec()