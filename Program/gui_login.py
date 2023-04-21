from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic
import sys
from gui_register import UI_register
from gui_forgot_password import UI_forgot_password
from gui_main_window import UI_main_window


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

        # creating textFields objects so we can use them later in the button's actions
        self.txt_username = self.findChild(QTextEdit, "txt_username")
        self.txt_password = self.findChild(QTextEdit, "txt_password")

        self.show()

    def button_register_pushed(self):
        self.clear_window()

        register_window = UI_register(self)
        register_window.closed.connect(self.show_this_window)  # connect the closed signal to the showWindow method

        self.close()
        register_window.show()

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

        main_window = UI_main_window(self)
        main_window.closed.connect(self.show_this_window)  # connect the closed signal to the showWindow method

        self.close()
        main_window.show()

    def show_this_window(self):
        self.show()

    def clear_window(self):
        self.txt_username.clear()
        self.txt_password.clear()


app = QApplication(sys.argv)
UIWindow = UI_login()
app.exec_()