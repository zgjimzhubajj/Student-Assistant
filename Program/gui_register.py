from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal


class UI_register(QMainWindow):
    closed = pyqtSignal()


    def __init__(self, parent=None):
        super(UI_register, self).__init__(parent)
        uic.loadUi("gui_register.ui", self)
        self.btn_cancel = self.findChild(QPushButton, "btn_cancel")
        self.btn_cancel.clicked.connect(self.button_cancel_pushed)

        self.btn_register = self.findChild(QPushButton, "btn_register")
        self.btn_register.clicked.connect(self.button_register_pushed)

    def button_cancel_pushed(self):
        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window

    def button_register_pushed(self):
        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window