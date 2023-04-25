from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QListWidget
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal


class UI_see_session_window(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(UI_see_session_window, self).__init__(parent)
        uic.loadUi("gui_see_session_window.ui", self)

        # buttons object
        self.btn_back = self.findChild(QPushButton, "btn_back")

        # buttons actions
        self.btn_back.clicked.connect(self.button_back_pushed)

        # list widget object
        self.list_widget_session_list = self.findChild(QListWidget, "list_widget_session_list")
        self.list_widget_session_detail = self.findChild(QListWidget, "list_widget_session_detail")
        self.list_widget_session_member_homework_detail = self.findChild(QListWidget, "list_widget_session_member_homework_detail")

    def button_back_pushed(self):
        self.clear_window()

        self.closed.emit()
        self.close()

    def clear_window(self):
        self.list_widget_session_list.clear()
        self.list_widget_session_detail.clear()
        self.list_widget_session_member_homework_detail.clear()
