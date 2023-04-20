from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal


class UI_register(QMainWindow):
    closed = pyqtSignal()


    def __init__(self, parent=None):
        super(UI_register, self).__init__(parent)
        uic.loadUi("gui_register.ui", self)
        self.btn_cancel = self.findChild(QPushButton, "btn_cancel")
        self.btn_cancel.clicked.connect(self.open_login_window)


    def open_login_window(self):
        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window
