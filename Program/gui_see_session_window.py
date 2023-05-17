from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QListWidget, QComboBox, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from controller import Controller


class UI_see_session_window(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None, user_name=None):
        super(UI_see_session_window, self).__init__(parent)
        uic.loadUi("gui_see_session_window.ui", self)
        self.user_name = user_name
        self.cntrl = Controller()

        # buttons object
        self.btn_mark_as_done = self.findChild(QPushButton, "btn_mark_as_done")
        self.btn_back = self.findChild(QPushButton, "btn_back")

        # buttons actions
        self.btn_mark_as_done.clicked.connect(self.button_mark_as_done_pushed)
        self.btn_back.clicked.connect(self.button_back_pushed)

        # label obejcts
        self.lbl_homework_details = self.findChild(QLabel, "lbl_homework_details")

        # list widget object
        self.list_widget_session_member_homework_detail = self.findChild(QListWidget, "list_widget_session_member_homework_detail")

        # combo_box objects
        self.combo_box_Sessions = self.findChild(QComboBox, "combo_box_Sessions")
        self.combo_box_members = self.findChild(QComboBox, "combo_box_members")
        self.combo_box_personal_homeworks = self.findChild(QComboBox, "combo_box_personal_homeworks")

        # combo_box actions
        self.combo_box_Sessions.currentIndexChanged.connect(self.combo_box_Sessions_changed)
        self.combo_box_members.currentIndexChanged.connect(self.combo_box_members_changed)
        self.combo_box_personal_homeworks.currentIndexChanged.connect(self.combo_box_personal_homeworks_changed)

        # window settings
        self.combo_box_members.setEnabled(False)
        self.combo_box_personal_homeworks.setEnabled(False)
        self.btn_mark_as_done.setEnabled(False)
        self.session_name_list = self.cntrl.get_sessions_names(self.user_name)
        self.session_name_list.insert(0, "")
        self.combo_box_Sessions.addItems(self.session_name_list)
        self.combo_box_Sessions.setCurrentIndex(0)

    # button actions
    def button_mark_as_done_pushed(self):
            if self.homework_index != 0:
                for index, tuple in enumerate(self.homeworks_tuple_list):
                    if index == (self.homework_index - 1):
                        if self.cntrl.check_if_homework_finished_before(tuple[1], self.user_name):
                            QMessageBox.information(self, "Error", "This homework already marked as finish")
                        else:
                            self.cntrl.mark_homework_as_done(tuple[1], self.user_name)
                self.combo_box_personal_homeworks.setCurrentIndex(0)
                self.list_widget_session_member_homework_detail.clear()
                self.homeworks_tuple_list_bool = self.cntrl.get_homework_bool(self.students_session_tuple[self.member_index - 1])
                for homework_bool_tuple in self.homeworks_tuple_list_bool:
                    homework_detail = ""
                    for indexx, value in enumerate(homework_bool_tuple):
                        if indexx == 0:
                            homework_detail = value[0]
                        else:
                            homework_detail = homework_detail + " " + value
                    self.list_widget_session_member_homework_detail.addItem(homework_detail)

    def button_back_pushed(self):
        # self.clear_window()
        self.closed.emit()
        self.close()

    # combo_box actions
    def combo_box_Sessions_changed(self, index):
        if index == 0:
            pass
        else:
            self.combo_box_members.setEnabled(True)
            self.session_name = self.combo_box_Sessions.itemText(index)
            self.combo_box_members.clear()
            self.students_session_tuple = self.cntrl.get_students_session(self.session_name, self.user_name)
            self.students_session = []
            self.students_session.insert(0, "")
            for tuple in self.students_session_tuple:
                self.students_session.append(tuple[0])
            self.combo_box_members.clear()
            self.combo_box_members.addItems(self.students_session)
            self.combo_box_members.setCurrentIndex(0)

    def combo_box_members_changed(self, index):
        if index == 0:
            self.lbl_homework_details.setText("")
            self.list_widget_session_member_homework_detail.clear()
        else:
            self.list_widget_session_member_homework_detail.clear()
            self.member_name = self.combo_box_members.itemText(index)
            self.member_index = index
            first_name, last_name = self.cntrl.get_first_name_last_name(self.user_name)
            first_name_last_name_of_user = first_name + " " + last_name
            self.lbl_homework_details.setText(f"Homework details of {self.member_name}")
            if self.member_name == first_name_last_name_of_user:
                self.combo_box_personal_homeworks.setEnabled(True)
                self.btn_mark_as_done.setEnabled(True)
                self.homeworks_tuple_list = self.cntrl.get_homeworks_names(self.user_name)
                self.homeworks_name_list = []
                for tuple in self.homeworks_tuple_list:
                    self.homeworks_name_list.append(tuple[0])
                self.homeworks_name_list.insert(0, "")
                self.combo_box_personal_homeworks.addItems(self.homeworks_name_list)
            else:
                self.combo_box_personal_homeworks.setEnabled(False)
                self.btn_mark_as_done.setEnabled(False)
                self.combo_box_personal_homeworks.clear()
            self.homeworks_tuple_list_bool = self.cntrl.get_homework_bool(self.students_session_tuple[self.member_index - 1])
            for homework_bool_tuple in self.homeworks_tuple_list_bool:
                homework_detail = ""
                for indexx, value in enumerate(homework_bool_tuple):
                    if indexx == 0:
                        homework_detail = value[0]
                    else:
                        homework_detail = homework_detail + " " + value
                self.list_widget_session_member_homework_detail.addItem(homework_detail)

    def combo_box_personal_homeworks_changed(self, index):
        self.homework_index = index
