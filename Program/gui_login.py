from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
import sys
from gui_register import UI_register
from gui_forgot_password import UI_forgot_password
from gui_main_window import UI_main_window


class UI_login(QMainWindow):
    def __init__(self):
        super(UI_login, self).__init__()
        uic.loadUi("gui_login.ui", self)
        self.btn_register = self.findChild(QPushButton, "btn_register")
        self.btn_register.clicked.connect(self.open_register_window)
        self.btn_forgot_password = self.findChild(QPushButton, "btn_forgot_password")
        self.btn_forgot_password.clicked.connect(self.open_forgot_password_window)
        self.btn_login = self.findChild(QPushButton, "btn_login")
        self.btn_login.clicked.connect(self.open_main_window)
        self.show()

    def open_register_window(self):
        register_window = UI_register(self)
        register_window.closed.connect(self.show_this_window)  # connect the closed signal to the showWindow method
        self.close()
        register_window.show()

    def open_forgot_password_window(self):
        forgot_password_window = UI_forgot_password(self)
        forgot_password_window.closed.connect(self.show_this_window)  # connect the closed signal to the showWindow method
        self.close()
        forgot_password_window.show()
    
    def open_main_window(self):
        main_window = UI_main_window(self)
        main_window.closed.connect(self.show_this_window)  # connect the closed signal to the showWindow method
        self.close()
        main_window.show()

    def show_this_window(self):
        self.show()


app = QApplication(sys.argv)
UIWindow = UI_login()
app.exec_()