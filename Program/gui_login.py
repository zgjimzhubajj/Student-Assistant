from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLabel
from PyQt5 import uic
import sys
from gui_register import UI_register
from gui_forgot_password import UI_forgot_password
from gui_main_window import UI_main_window
from controller import Controller


class UI_login(QMainWindow):
    def __init__(self):
        super(UI_login, self).__init__()
        uic.loadUi("gui_login.ui", self)

        # creating buttons
        self.btn_register = self.findChild(QPushButton, "btn_register")
        self.btn_forgot_password = self.findChild(QPushButton, "btn_forgot_password")
        self.btn_login = self.findChild(QPushButton, "btn_login")

        # creating actions for buttons
        self.btn_register.clicked.connect(self.button_register_pushed)
        self.btn_forgot_password.clicked.connect(self.button_forgot_password_pushed)
        self.btn_login.clicked.connect(self.button_login_pushed)

        # label object
        self.lbl_wrong_input = self.findChild(QLabel, "lbl_wrong_input")

        # creating textFields objects so we can use them later in the button's actions
        self.txt_username = self.findChild(QTextEdit, "txt_username")
        self.txt_password = self.findChild(QTextEdit, "txt_password")

        # when window open settings for combobox and spinbox
        self.lbl_wrong_input.setStyleSheet("color: red")

        self.show()

    def button_register_pushed(self):
        self.clear_window()

        self.register_window = UI_register(self)
        self.register_window.closed.connect(self.show_this_window)  # connect the closed signal to the showWindow method

        self.close()
        self.register_window.show()

    def button_forgot_password_pushed(self):
        self.clear_window()

        forgot_password_window = UI_forgot_password(self)
        forgot_password_window.closed.connect(self.show_this_window)  # connect the closed signal to the showWindow method

        self.close()
        forgot_password_window.show()

    def button_login_pushed(self):
        username = self.txt_username.toPlainText()
        password = self.txt_password.toPlainText()
        self.clear_window()
        self.cntrl = Controller()
        if self.cntrl.check_login_stats(username, password):
            self.main_window = UI_main_window(self)
            self.main_window.closed.connect(self.show_this_window)  # connect the closed signal to the showWindow method
            self.close()
            self.main_window.show()
        else:
            self.lbl_wrong_input.setText("Wong name or password!")

    def show_this_window(self):
        self.show()

    def clear_window(self):
        self.txt_username.clear()
        self.txt_password.clear()
        self.lbl_wrong_input.setText("")


app = QApplication(sys.argv)
UIWindow = UI_login()
app.exec_()
