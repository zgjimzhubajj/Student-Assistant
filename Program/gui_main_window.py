from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from gui_create_session_window import UI_create_session_window
from gui_see_session_window import UI_see_session_window
from controller import Controller


class UI_main_window(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None, username=None):
        super(UI_main_window, self).__init__(parent)
        uic.loadUi("gui_main_window.ui", self)
        self.username = username
        self.cntrl = Controller()

    # buttons objects
        # team session tab
        self.btn_log_out = self.findChild(QPushButton, "btn_log_out")
        self.btn_ts_create_session = self.findChild(QPushButton, "btn_ts_create_session")
        self.btn_ts_see_session = self.findChild(QPushButton, "btn_ts_see_session")
        # time manegement tab

        # material tab

    # buttons actions
        # team session tab
        self.btn_log_out.clicked.connect(self.button_log_out_pushed)
        self.btn_ts_create_session.clicked.connect(self.button_ts_create_session_pushed)
        self.btn_ts_see_session.clicked.connect(self.button_ts_see_session_pushed)
        # time manegement tab

        # material tab

    # label objects
        # team session tab
        self.lbl_ts_time_left_for_next_homework_1 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_1")
        self.lbl_ts_time_left_for_next_homework_2 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_2")
        self.lbl_ts_time_left_for_next_homework_3 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_3")
        self.lbl_ts_time_left_for_next_homework_4 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_4")
        self.lbl_ts_time_left_for_next_homework_5 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_5")
        # time manegement tab

        # material tab

    # list objects
        # team session tab
        self.list_widget_ts_homework = self.findChild(QListWidget, "list_widget_ts_homework")
        self.list_widget_homework_detail = self.findChild(QListWidget, "list_widget_homework_detail")
        # time management tab

        # material tab

    # window settings when window open
        # team session tab
        self.list_widget_ts_homework.addItems(self.cntrl.get_course(username))
        self.list_widget_homework_detail.clear()
        # time manegement tab

        # material tab

    # actions for list widget objects
        # team session tab
        self.list_widget_ts_homework.itemClicked.connect(self.text_clicked_item_homeworks)

        # time manegement tab

        # material tab

# methods for buttons action
    # team session tab
    def button_log_out_pushed(self):
        self.clear_window()
        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window

    def button_ts_create_session_pushed(self):
        self.clear_window()
        self.create_session_window = UI_create_session_window(self)
        self.create_session_window.closed.connect(self.show_this_window)
        self.close()
        self.create_session_window.show()

    def button_ts_see_session_pushed(self):
        self.clear_window()
        self.see_session_window = UI_see_session_window(self)
        self.see_session_window.closed.connect(self.show_this_window)
        self.close()
        self.see_session_window.show()

    # time manegement tab

    # material tab

# methods for list widget actions
    # team session tab
    def text_clicked_item_homeworks(self, item):
        self.list_widget_homework_detail.clear()
        course_name = item.text()
        homework_list = self.cntrl.get_homework_detail(course_name)
        for homework in homework_list:
            homework_details = "Homework name: " + homework[0] + " " + " Homework deadline: " + homework[1] + "/" + homework[2] + "/" + homework[3]
            self.list_widget_homework_detail.addItem(homework_details)

    # time manegement tab

    # material tab

# methods for main window
    def show_this_window(self):
        self.show()

    def clear_window(self):
        self.lbl_ts_time_left_for_next_homework_1.setText("")
        self.lbl_ts_time_left_for_next_homework_2.setText("")
        self.lbl_ts_time_left_for_next_homework_3.setText("")
        self.lbl_ts_time_left_for_next_homework_4.setText("")
        self.lbl_ts_time_left_for_next_homework_5.setText("")
        self.list_widget_homework_detail.clear()
