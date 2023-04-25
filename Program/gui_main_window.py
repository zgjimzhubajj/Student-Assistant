from PyQt5.QtWidgets import QMainWindow, QTabWidget, QPushButton, QWidget, QListView, QLabel, QListWidget
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal


class UI_main_window(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None, username=None):
        super(UI_main_window, self).__init__(parent)
        uic.loadUi("gui_main_window.ui", self)
        self.username = username

        # buttons objects
        # team session tab buttons
        self.btn_log_out = self.findChild(QPushButton, "btn_log_out")
        self.btn_ts_create_session = self.findChild(QPushButton, "btn_ts_create_session")
        self.btn_ts_see_session = self.findChild(QPushButton, "btn_ts_see_session")
        # time manegement tab buttons

        # material tab buttons

        # buttons actions
        # button actions for team session tab
        self.btn_log_out.clicked.connect(self.button_log_out_pushed)
        self.btn_ts_create_session.clicked.connect(self.button_ts_create_session_pushed)
        self.btn_ts_see_session.clicked.connect(self.button_ts_see_session_pushed)
        # time manegement tab buttons actions
        
        # material tab buttons actions

        # label objects
        # team session labels
        self.lbl_ts_time_left_for_next_homework_1 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_1")
        self.lbl_ts_time_left_for_next_homework_2 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_2")
        self.lbl_ts_time_left_for_next_homework_3 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_3")
        self.lbl_ts_time_left_for_next_homework_4 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_4")
        self.lbl_ts_time_left_for_next_homework_5 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_5")
        # time manegement tab labels

        # material tab labels

        # tab window object
        self.tab_main_window = self.findChild(QTabWidget, "tab_main_window")
        self.tab_team_session = self.findChild(QWidget, "tab_team_session")

        # list objects
        # list ogject for team session tab
        self.list_widget_1 = self.findChild(QListWidget, "list_widget_1")
        self.list_widget_2 = self.findChild(QListWidget, "list_widget_2")
        # list ogject for time manegement tab

        # list ogject for material tab

        # window settings when window open
        # window setting for team session tab
        entries = ["a", "b"]
        self.list_widget_2.addItems(entries)
        self.list_widget_1.clear()
        index_of_item_clicked = self.list_widget_1.currentRow()
        store_item_taken_from_list = self.list_widget_1.takeItem(index_of_item_clicked) # this will take the item out of the list
        # window setting for time manegement tab

        # window setting for material tab

# methods for buttons action for team session tab
    def button_log_out_pushed(self):
        self.clear_window()
        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window

    def button_ts_create_session_pushed(self):
        pass

    def button_ts_see_session_pushed(self):
        pass

    def clear_window(self):
        self.lbl_ts_time_left_for_next_homework_1.setText("")
        self.lbl_ts_time_left_for_next_homework_2.setText("")
        self.lbl_ts_time_left_for_next_homework_3.setText("")
        self.lbl_ts_time_left_for_next_homework_4.setText("")
        self.lbl_ts_time_left_for_next_homework_5.setText("")
# always use line edit and we use .text() to get the text and .setText() to set a text in it

# methods for buttons action for time manegement tab

# methods for buttons action for material tab
