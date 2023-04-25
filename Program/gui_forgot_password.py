from PyQt5.QtWidgets import QMainWindow, QPushButton, QTextEdit, QComboBox, QSpinBox, QLabel
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from controller import Controller


class UI_forgot_password(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(UI_forgot_password, self).__init__(parent)
        uic.loadUi("gui_forgot_password.ui", self)

        # label object
        self.lbl_wrong_input = self.findChild(QLabel, "lbl_wrong_input")

        # buttons objects
        self.btn_cancel = self.findChild(QPushButton, "btn_cancel")
        self.btn_ok = self.findChild(QPushButton, "btn_ok")

        # buttons actions
        self.btn_ok.clicked.connect(self.button_ok_pushed)
        self.btn_cancel.clicked.connect(self.button_cancel_pushed)

        # textfield objects
        self.txt_first_name = self.findChild(QTextEdit, "txt_first_name")
        self.txt_last_name = self.findChild(QTextEdit, "txt_last_name")
        self.txt_email = self.findChild(QTextEdit, "txt_email")
        self.txt_username = self.findChild(QTextEdit, "txt_username")
        self.txt_personal_id = self.findChild(QTextEdit, "txt_personal_id")

        # spinBox object
        self.spin_box_year_of_study = self.findChild(QSpinBox, "spin_box_year_of_study")

        # comboBox object
        self.combo_box_name_of_program = self.findChild(QComboBox, "combo_box_name_of_program")

        self.cntrl = Controller()

        # window's settings
        self.combo_box_name_of_program.addItems(self.cntrl.get_programs_info_from_database())
        self.spin_box_year_of_study.setEnabled(False)
        self.combo_box_name_of_program.currentIndexChanged.connect(self.handle_program_change)
        self.lbl_wrong_input.setStyleSheet("color: red")

    def button_cancel_pushed(self):
        self.clear_window()
        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window

    def button_ok_pushed(self):
        self.get_window_values()
        self.wrong_inputs = True
        self.check_input()
        if self.wrong_inputs:
            password = self.cntrl.retrieve_password(self.first_name, self.last_name, self.email, self.username, self.personal_id, self.year_of_study, self.name_of_program)
            self.lbl_wrong_input.setText(password)
            self.clear_window()

    def clear_window(self):
        self.txt_first_name.clear()
        self.txt_last_name.clear()
        self.txt_email.clear()
        self.txt_username.clear()
        self.txt_personal_id.clear()
        self.spin_box_year_of_study.setValue(0)
        self.combo_box_name_of_program.setCurrentIndex(-1)
        self.lbl_wrong_input.setText("")

    def handle_program_change(self, index):
        if index == 0:  # No item selected in the combobox
            self.spin_box_year_of_study.setEnabled(False)
        else:
            self.spin_box_year_of_study.setEnabled(True)
            if self.combo_box_name_of_program.currentText() == "Medicine":
                self.spin_box_year_of_study.setMinimum(1)
                self.spin_box_year_of_study.setMaximum(5)
            else:
                self.spin_box_year_of_study.setMinimum(1)
                self.spin_box_year_of_study.setMaximum(3)

    def get_window_values(self):
        self.first_name = self.txt_first_name.toPlainText()
        self.last_name = self.txt_last_name.toPlainText()
        self.email = self.txt_email.toPlainText()
        self.username = self.txt_username.toPlainText()
        self.personal_id = self.txt_personal_id.toPlainText()
        self.year_of_study = self.spin_box_year_of_study.value()
        self.name_of_program = self.combo_box_name_of_program.currentText()

    def check_input(self):
        self.get_window_values()
        num_chars1 = len(self.first_name)
        num_chars2 = len(self.last_name)
        num_chars3 = len(self.email)
        num_at = self.email.count("@")
        num_chars4 = len(self.username)
        num_chars7 = len(self.personal_id)
        if num_chars1 > 50 or num_chars1 < 1:
            self.lbl_wrong_input.setText("First name is not in range of 1 to 50 characters!")
            self.wrong_inputs = False
        elif self.first_name.strip() == "":
            self.lbl_wrong_input.setText("You must write something as first name!")
            self.wrong_inputs = False
        elif num_chars2 > 50 or num_chars2 < 1:
            self.lbl_wrong_input.setText("Last name is not in range of 1 to 50 characters!")
            self.wrong_inputs = False
        elif self.last_name.strip() == "":
            self.lbl_wrong_input.setText("You must write something as last name!")
            self.wrong_inputs = False
        elif num_chars3 > 50 or num_chars3 < 1:
            self.lbl_wrong_input.setText("Email is not in range of 1 to 50 characters!")
            self.wrong_inputs = False
        elif self.email.strip() == "":
            self.lbl_wrong_input.setText("You must write something as email!")
            self.wrong_inputs = False
        elif "@" not in self.email and "." not in self.email:
            self.lbl_wrong_input.setText("You must make sure to include '@' and '.' in email!")
            self.wrong_inputs = False
        elif num_at != 1:
            self.lbl_wrong_input.setText("You must make sure to include one '@' only!")
            self.wrong_inputs = False
        elif num_chars4 > 50 or num_chars4 < 1:
            self.lbl_wrong_input.setText("UserName is not in range of 1 to 50 characters!")
            self.wrong_inputs = False
        elif self.username.strip() == "":
            self.lbl_wrong_input.setText("You must write something as userName!")
            self.wrong_inputs = False
        elif not self.cntrl.check_user_name_exists(self.username):
            self.lbl_wrong_input.setText("Username doesn't exist in the database.")
            self.wrong_inputs = False
        elif self.combo_box_name_of_program.currentText() == "":
            self.lbl_wrong_input.setText("You must choose a program!")
            self.wrong_inputs = False
        elif num_chars7 != 10:
            self.lbl_wrong_input.setText("Personal ID must be a 10 digit number!")
            self.wrong_inputs = False
        elif self.personal_id.strip() == "":
            self.lbl_wrong_input.setText("You must write your personal ID!")
            self.wrong_inputs = False
        elif not self.personal_id.isdigit():
            self.lbl_wrong_input.setText("Personal ID must be numbers only!")
            self.wrong_inputs = False
