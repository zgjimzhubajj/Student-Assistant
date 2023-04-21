from PyQt5.QtWidgets import QMainWindow, QPushButton, QTextEdit, QComboBox, QSpinBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal


class UI_forgot_password(QMainWindow):
    closed = pyqtSignal()


    def __init__(self, parent=None):
        super(UI_forgot_password, self).__init__(parent)
        uic.loadUi("gui_forgot_password.ui", self)

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

    def button_cancel_pushed(self):
        self.clear_window()

        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window

    def button_ok_pushed(self):
        first_name = self.txt_first_name.toPlainText()
        last_name = self.txt_last_name.toPlainText()
        email = self.txt_email.toPlainText()
        username = self.txt_username.toPlainText()
        personal_id = self.txt_personal_id.toPlainText()
        year_of_study = self.spin_box_year_of_study.value()
        name_of_program = self.combo_box_name_of_program.currentText()

        self.clear_window()

        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window

    def clear_window(self):
        self.txt_first_name.clear()
        self.txt_last_name.clear()
        self.txt_email.clear()
        self.txt_username.clear()
        self.txt_personal_id.clear()
        self.spin_box_year_of_study.setValue(0)
        self.combo_box_name_of_program.setCurrentIndex(-1)
