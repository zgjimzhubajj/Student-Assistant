from PyQt5.QtWidgets import QMainWindow, QPushButton, QComboBox, QListWidget, QLabel, QLineEdit, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from controller import Controller


class UI_create_session_window(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None, user_name=None):
        super(UI_create_session_window, self).__init__(parent)
        uic.loadUi("gui_create_session_window.ui", self)
        # object of controller class
        self.cntrl = Controller()
        self.user_name = user_name
        self.student_session_list = []

        # buttons object
        self.btn_save_session_name = self.findChild(QPushButton, "btn_save_session_name")
        self.btn_add_student = self.findChild(QPushButton, "btn_add_student")
        self.btn_back = self.findChild(QPushButton, "btn_back")
        self.btn_create_session = self.findChild(QPushButton, "btn_create_session")

        # buttons actions
        self.btn_save_session_name.clicked.connect(self.button_save_session_name_pushed)
        self.btn_add_student.clicked.connect(self.button_add_student_pushed)
        self.btn_back.clicked.connect(self.button_back_pushed)
        self.btn_create_session.clicked.connect(self.button_create_session_pushed)

        # comboBox object
        self.combo_box_student_name = self.findChild(QComboBox, "combo_box_student_name")

        # label obejcts
        self.lbl_session_info = self.findChild(QLabel, "lbl_session_info")
        self.lbl_wrong_inputs = self.findChild(QLabel, "lbl_wrong_inputs")

        # line edit object
        self.line_edit_name_of_session = self.findChild(QLineEdit, "line_edit_name_of_session")

        # list objects
        self.list_widget_member_of_session = self.findChild(QListWidget, "list_widget_member_of_session")

        # window settings
        self.get_student_list()
        for tuple in self.student_list:
            self.combo_box_student_name.addItem(tuple[0])
        self.combo_box_student_name.currentIndexChanged.connect(self.combo_box_student_name_change)
        self.lbl_wrong_inputs.setStyleSheet("color: red")
        self.combo_box_student_name.setEnabled(False)
        self.btn_add_student.setEnabled(False)
        self.btn_create_session.setEnabled(False)

    # methods for buttons actions
    def button_save_session_name_pushed(self):
        if self.line_edit_name_of_session.text().strip() == "":
            self.lbl_wrong_inputs.setText("You must not leave session name empty")
        else:
            self.session_name = self.line_edit_name_of_session.text()
            if not self.cntrl.check_session_name(self.session_name, self.user_name):
                self.lbl_wrong_inputs.setText("")
                self.line_edit_name_of_session.clear()
                self.lbl_session_info.setText(f"Members of {self.session_name}:")
                self.combo_box_student_name.setEnabled(True)
                self.btn_add_student.setEnabled(True)
            else:
                self.lbl_wrong_inputs.setText("Session name already exist")

    def button_add_student_pushed(self):
        if self.student_list == [('', 0)]:
            self.btn_add_student.setEnabled(False)
        else:
            self.student_session_list.append(self.student_list[self.index])
            self.list_widget_member_of_session.addItem(self.selected_student)
            self.btn_create_session.setEnabled(True)
            del self.student_list[self.index]
            self.combo_box_student_name.clear()
            for tuple in self.student_list:
                self.combo_box_student_name.addItem(tuple[0])

    def button_back_pushed(self):
        self.clear_window()
        self.closed.emit()
        self.close()

    def button_create_session_pushed(self):
        if self.cntrl.check_session_members(self.student_session_list, self.user_name):
            QMessageBox.information(self, "Error", "Those members already exist in this session")
            self.clear_window()
            self.combo_box_student_name.setEnabled(False)
            self.btn_add_student.setEnabled(False)
            self.btn_create_session.setEnabled(False)
        else:
            self.cntrl.store_session(self.session_name, self.user_name)
            session_id = self.cntrl.get_session_id(self.session_name, self.user_name)
            self.cntrl.store_students_in_session(self.student_session_list, session_id)
            self.clear_window()
            self.closed.emit()
            self.close()

    # extra methods
    def get_student_list(self):
        self.student_list = self.cntrl.get_students(self.user_name)
        first_name, last_name = self.cntrl.get_first_name_last_name(self.user_name)
        name = first_name + " " + last_name
        for index, tuple in enumerate(self.student_list):
            if tuple[0] == name:
                self.student_session_list.append(self.student_list[index])
                del self.student_list[index]

    # methods for combo box actions
    def combo_box_student_name_change(self, index):
        self.selected_student = self.combo_box_student_name.itemText(index)
        self.index = index

    def clear_window(self):
        self.line_edit_name_of_session.clear()
        self.combo_box_student_name.clear()
        self.student_session_list = []
        self.get_student_list()
        for tuple in self.student_list:
            self.combo_box_student_name.addItem(tuple[0])
        self.combo_box_student_name.setCurrentIndex(0)
        self.lbl_session_info.setText("")
        self.list_widget_member_of_session.clear()
        self.lbl_wrong_inputs.setText("")
