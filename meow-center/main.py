from PySide6.QtWidgets import *

app = QApplication([])

window = QWidget()
window.setWindowTitle("Meow Center")

layout = QVBoxLayout()

title = QLabel("Meow OS")
layout.addWidget(title)

layout.addWidget(QPushButton("Build EXE"))
layout.addWidget(QPushButton("Run Python"))
layout.addWidget(QPushButton("Check Updates"))
layout.addWidget(QPushButton("System Info"))

window.setLayout(layout)
window.resize(400, 250)

window.show()

app.exec()