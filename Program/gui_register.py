from PyQt5.QtWidgets import QMainWindow, QPushButton, QTextEdit, QComboBox, QSpinBox, QLabel
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from controller import Controller
from PyQt5.QtCore import QSize


class UI_register(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(UI_register, self).__init__(parent)
        uic.loadUi("gui_register.ui", self)

        # buttons objects
        self.btn_cancel = self.findChild(QPushButton, "btn_cancel")
        self.btn_register = self.findChild(QPushButton, "btn_register")

        # buttons actions
        self.btn_register.clicked.connect(self.button_register_pushed)
        self.btn_cancel.clicked.connect(self.button_cancel_pushed)

        # textfield objects
        self.txt_first_name = self.findChild(QTextEdit, "txt_first_name")
        self.txt_last_name = self.findChild(QTextEdit, "txt_last_name")
        self.txt_email = self.findChild(QTextEdit, "txt_email")
        self.txt_username = self.findChild(QTextEdit, "txt_username")
        self.txt_password = self.findChild(QTextEdit, "txt_password")
        self.txt_repeat_password = self.findChild(QTextEdit, "txt_repeat_password")
        self.txt_personal_id = self.findChild(QTextEdit, "txt_personal_id")

        # label object
        self.lbl_wrong_input = self.findChild(QLabel, "lbl_wrong_input")

        # spinBox object
        self.spin_box_year_of_study = self.findChild(QSpinBox, "spin_box_year_of_study")

        # comboBox object
        self.combo_box_name_of_program = self.findChild(QComboBox, "combo_box_name_of_program")

        # object of controller class
        self.cntrl = Controller()

        # when window open settings for combobox and spinbox
        self.combo_box_name_of_program.addItems(self.cntrl.get_programs_info_from_database())
        self.spin_box_year_of_study.setEnabled(False)
        self.combo_box_name_of_program.currentIndexChanged.connect(self.handle_program_change)
        self.lbl_wrong_input.setStyleSheet("color: red")

    def button_cancel_pushed(self):
        self.clear_window()

        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window

    def button_register_pushed(self):
        self.get_window_values()
        self.wrong_inputs = True

        self.check_input()

        if self.wrong_inputs:
            self.cntrl.register_student_in_database(self.first_name, self.last_name, self.email, self.username, self.password, self.personal_id, self.year_of_study, self.name_of_program)

            self.clear_window()

            self.closed.emit()  # emit the closed signal
            self.close()  # close the new window

# shortcuts methods
    def clear_window(self):
        self.txt_first_name.clear()
        self.txt_last_name.clear()
        self.txt_email.clear()
        self.txt_username.clear()
        self.txt_password.clear()
        self.txt_repeat_password.clear()
        self.txt_personal_id.clear()
        self.spin_box_year_of_study.setValue(0)
        self.combo_box_name_of_program.setCurrentIndex(-1)

    def get_window_values(self):
        self.first_name = self.txt_first_name.toPlainText()
        self.last_name = self.txt_last_name.toPlainText()
        self.email = self.txt_email.toPlainText()
        self.username = self.txt_username.toPlainText()
        self.password = self.txt_password.toPlainText()
        self.repeat_password = self.txt_repeat_password.toPlainText()
        self.personal_id = self.txt_personal_id.toPlainText()
        self.year_of_study = self.spin_box_year_of_study.value()
        self.name_of_program = self.combo_box_name_of_program.currentText()

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

# error handling methods for the textfields and spin box
    def check_input(self):
        self.get_window_values()
        num_chars1 = len(self.first_name)
        num_chars2 = len(self.last_name)
        num_chars3 = len(self.email)
        num_at = self.email.count("@")
        num_chars4 = len(self.username)
        num_chars5 = len(self.password)
        num_chars6 = len(self.repeat_password)
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
        elif self.cntrl.check_user_name_exists(self.username):
            self.lbl_wrong_input.setText("Username is already taken. Please choose another one!")
            self.wrong_inputs = False
        elif num_chars5 > 50 or num_chars5 < 1:
            self.lbl_wrong_input.setText("Password is not in range of 1 to 50 characters!")
            self.wrong_inputs = False
        elif self.password.strip() == "":
            self.lbl_wrong_input.setText("You must write something as password!")
            self.wrong_inputs = False
        elif num_chars6 > 50 or num_chars6 < 1:
            self.lbl_wrong_input.setText("Repeat password is not in range of 1 to 50 characters!")
            self.wrong_inputs = False
        elif self.repeat_password.strip() == "":
            self.lbl_wrong_input.setText("You must write something as repeat password!")
            self.wrong_inputs = False
        elif self.password != self.repeat_password:
            self.lbl_wrong_input.setText("Password and repeat password must match!")
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
