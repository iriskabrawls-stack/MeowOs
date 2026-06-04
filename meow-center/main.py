from PySide6.QtWidgets import *

app = QApplication([])

window = QWidget()
window.setWindowTitle("Meow Center")

layout = QVBoxLayout()

layout.addWidget(QLabel("Meow OS 0.1"))

layout.addWidget(QPushButton("Build EXE"))
layout.addWidget(QPushButton("Run EXE"))
layout.addWidget(QPushButton("Check Updates"))

window.setLayout(layout)
window.resize(400, 250)

window.show()

app.exec()
