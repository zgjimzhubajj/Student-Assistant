from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal


class UI_main_window(QMainWindow):
    closed = pyqtSignal()


    def __init__(self, parent=None):
        super(UI_main_window, self).__init__(parent)
        uic.loadUi("gui_main_window.ui", self)
        self.btn_log_out = self.findChild(QPushButton, "btn_log_out")
        self.btn_log_out.clicked.connect(self.button_log_out_pushed)

    def button_log_out_pushed(self):
        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window
