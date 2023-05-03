from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSignal


class UI_dialog_window(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(UI_dialog_window, self).__init__(parent)
        self.main_window = parent
        uic.loadUi("gui_dialog.ui", self)
        

        # buttons object
        self.btn_close = self.findChild(QPushButton, "btn_close")
        self.btn_add = self.findChild(QPushButton, "btn_add")

        # buttons actions
        self.btn_close.clicked.connect(self.button_close_pushed)
        self.btn_add.clicked.connect(self.button_add_pushed)

        # label objects
        self.lbl_wrong_input = self.findChild(QLabel, "lbl_wrong_input")

        # textfield objects
        self.txt_start_time = self.findChild(QLineEdit, "txt_start_time")
        self.txt_end_time = self.findChild(QLineEdit, "txt_end_time")
        self.txt_activity = self.findChild(QLineEdit, "txt_activity")


    def button_close_pushed(self):
        self.clear_window()
        self.closed.emit()
        self.close()

    def button_add_pushed(self):
        self.wrong_inputs = True
        self.check_input()
        if self.wrong_inputs:
            item_text = f"{self.start_time} - {self.end_time}: {self.activity}"
            self.main_window.add_dialog(item_text)
            self.clear_window()
            self.closed.emit()
            self.close()


    def clear_window(self):
        self.txt_start_time.clear()
        self.txt_end_time.clear()
        self.txt_activity.clear()
        self.lbl_wrong_input.setText("")

    def check_input(self):
        self.start_time = self.txt_start_time.text()
        self.end_time = self.txt_end_time.text()
        self.activity = self.txt_activity.text()
        num_chars1 = len(self.start_time)
        num_chars2 = len(self.end_time)
        if num_chars1 >= 24 or num_chars1 < 0:
            self.lbl_wrong_input.setText("start time must be 1 to 2 integers!")
            self.wrong_inputs = False
        elif self.start_time.strip() == "":
            self.lbl_wrong_input.setText("You must write something as start time!")
            self.wrong_inputs = False
        elif not self.start_time.isdigit():
            self.lbl_wrong_input.setText("Start time must be numbers only!")
            self.wrong_inputs = False
        elif num_chars2 >= 24 or num_chars2 < 0:
            self.lbl_wrong_input.setText("End time must be 1 to 2 integers!")
            self.wrong_inputs = False
        elif self.end_time.strip() == "":
            self.lbl_wrong_input.setText("You must write something as end time!")
            self.wrong_inputs = False
        elif not self.end_time.isdigit():
            self.lbl_wrong_input.setText("End time must be numbers only!")
            self.wrong_inputs = False
        elif self.activity.strip() == "":
            self.lbl_wrong_input.setText("You must write something as activity!")
            self.wrong_inputs = False
        elif self.start_time == self.end_time:
            self.lbl_wrong_input.setText("You must choose different hours for start and end time!")
            self.wrong_inputs = False
