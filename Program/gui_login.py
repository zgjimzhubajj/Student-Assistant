from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
import sys
from gui_register import UI_register



class UI_login(QMainWindow):
    def __init__(self):
        super(UI_login, self).__init__()
        uic.loadUi("gui_login.ui", self)
        self.btn_register = self.findChild(QPushButton, "btn_register")
        self.btn_register.clicked.connect(self.open_register_window)
        self.show()


    def open_register_window(self):
        register_window = UI_register(self)
        register_window.closed.connect(self.show_this_window)  # connect the closed signal to the showWindow method
        self.hide()
        register_window.show()


    def show_this_window(self):
        self.show()




app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()