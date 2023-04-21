from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal


class UI_forgot_password(QMainWindow):
    closed = pyqtSignal()


    def __init__(self, parent=None):
        super(UI_forgot_password, self).__init__(parent)
        uic.loadUi("gui_forgot_password.ui", self)
        self.btn_cancel = self.findChild(QPushButton, "btn_cancel")
        self.btn_cancel.clicked.connect(self.button_cancel_pushed)

        self.btn_ok = self.findChild(QPushButton, "btn_ok")
        self.btn_ok.clicked.connect(self.button_ok_pushed)

    def button_cancel_pushed(self):
        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window

    def button_ok_pushed(self):
        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window
