from PyQt5.QtWidgets import QMainWindow, QPushButton, QComboBox, QListWidget
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal


class UI_create_session_window(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(UI_create_session_window, self).__init__(parent)
        uic.loadUi("gui_create_session_window.ui", self)

        # buttons object
        self.btn_back = self.findChild(QPushButton, "btn_back")
        self.btn_add_course = self.findChild(QPushButton, "btn_add_course")
        self.btn_add_student = self.findChild(QPushButton, "btn_add_student")

        # buttons actions
        self.btn_back.clicked.connect(self.button_back_pushed)
        self.btn_add_course.clicked.connect(self.button_add_course_pushed)
        self.btn_add_student.clicked.connect(self.button_add_student_pushed)

        # comboBox object
        self.combo_box_name_program = self.findChild(QComboBox, "combo_box_name_program")
        self.combo_box_name_course = self.findChild(QComboBox, "combo_box_name_course")
        self.combo_box_student_name = self.findChild(QComboBox, "combo_box_student_name")

        # list widget object
        self.list_widget_added_info = self.findChild(QListWidget, "list_widget_added_info")

    def button_back_pushed(self):
        self.clear_window()
        self.closed.emit()
        self.close()

    def button_add_course_pushed(self):
        pass

    def button_add_student_pushed(self):
        pass

    def clear_window(self):
        self.combo_box_name_program.setCurrentIndex(-1)
        self.combo_box_name_course.setCurrentIndex(-1)
        self.combo_box_student_name.setCurrentIndex(-1)
        self.list_widget_added_info.clear()
