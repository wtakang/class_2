import random

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


def gen_password():
    length = int(plength.text())

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
    password = ''
  
    if msg.text():
        msg.setText("")
        plength.setText("")
    else:
        for c in range(length):
            password += random.choice(chars)
    msg.setText(password)


def clear_form():
    msg.setText("")
    plength.setText("")

# pyqt5 ui 
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Password Generator')
layout = QVBoxLayout()

layout.addWidget(QLabel('Enter desired password length'))

plength = QLineEdit('')
layout.addWidget(plength)

btn = QPushButton('Generate')
btn.clicked.connect(gen_password)
layout.addWidget(btn)

rbtn = QPushButton('Reset')
rbtn.clicked.connect(clear_form)
layout.addWidget(rbtn)

msg = QLineEdit('')
layout.addWidget(msg)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
