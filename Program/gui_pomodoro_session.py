from PyQt5.QtWidgets import QMainWindow, QPushButton, QComboBox, QListWidget, QLabel
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal


class UI_pomodoro_session(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(UI_pomodoro_session, self).__init__(parent)
        uic.loadUi("gui_pomodoro_session.ui", self)

        # buttons object
        self.btn_pause = self.findChild(QPushButton, "btn_pause")
        self.btn_resume = self.findChild(QPushButton, "btn_resume")
        self.btn_end_session = self.findChild(QPushButton, "btn_end_session")

        # buttons actions
        self.btn_pause.clicked.connect(self.button_pause_pushed)
        self.btn_resume.clicked.connect(self.button_resume_pushed)
        self.btn_end_session.clicked.connect(self.button_end_session_pushed)

        # list widget object
        self.list_widget_name_of_media = self.findChild(QListWidget, "list_widget_name_of_media")

        # label objects
        self.lbl_study_break_condition = self.findChild(QLabel, "lbl_study_break_condition")
        self.lbl_backwards_counter = self.findChild(QLabel, "lbl_backwards_counter")

    def button_end_session_pushed(self):
        self.clear_window()
        self.closed.emit()
        self.close()

    def button_pause_pushed(self):
        pass

    def button_resume_pushed(self):
        pass

    def clear_window(self):
        self.list_widget_name_of_media.clear()
        self.lbl_study_break_condition.setText("")
        self.lbl_backwards_counter.setText("")
