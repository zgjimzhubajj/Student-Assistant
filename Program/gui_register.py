from PyQt5.QtWidgets import QMainWindow, QPushButton, QTextEdit, QComboBox, QSpinBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from controller import Controller


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

    def button_cancel_pushed(self):
        self.clear_window()

        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window

    def button_register_pushed(self):
        first_name = self.txt_first_name.toPlainText()
        last_name = self.txt_last_name.toPlainText()
        email = self.txt_email.toPlainText()
        username = self.txt_username.toPlainText()
        password = self.txt_password.toPlainText()
        repeat_password = self.txt_repeat_password.toPlainText()
        personal_id = int(self.txt_personal_id.toPlainText())
        year_of_study = self.spin_box_year_of_study.value()
        name_of_program = self.combo_box_name_of_program.currentText()

        # check if any field left empty
        if first_name == "" or last_name == "" or email == "" or username == "" or password == "" or repeat_password == "" or personal_id == "" or name_of_program== "":
            pass
        elif len(first_name) > 50:
            pass
        elif len(last_name) > 50:
            pass
        elif len(email) > 50:
            pass
        elif email.count("@") != 1 or email.count(".") < 1:
            pass
        elif len(username) > 50:
            pass

        # check if username already exist in the database(not finished yet)

        elif len(password) > 50:
            pass
        elif len(repeat_password) > 50:
            pass
        elif password != repeat_password:
            pass
        # elif len(str(personal_id)) != 12:
        #     pass
        # elif type(personal_id) != int:
        #     pass
        else:
            self.cntrl.register_student_in_database(first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program)

        self.clear_window()

        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window

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
