from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal


class UI_note_window(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(UI_note_window, self).__init__(parent)
        uic.loadUi("gui_note_window.ui", self)

        # buttons object
        self.btn_back = self.findChild(QPushButton, "btn_back")
        self.btn_save = self.findChild(QPushButton, "btn_save")

        # buttons actions
        self.btn_back.clicked.connect(self.button_back_pushed)
        self.btn_save.clicked.connect(self.button_save_pushed)

        # line edit object
        self.line_edit_note_name = self.findChild(QLineEdit, "line_edit_note_name")
        self.line_edit_note = self.findChild(QLineEdit, "line_edit_note")

        # label object
        self.lbl_wrong_input = self.findChild(QLineEdit, "lbl_wrong_input")

    def button_back_pushed(self):
        self.clear_window()
        self.closed.emit()
        self.close()

    def button_save_pushed(self):
        self.clear_window()
        self.closed.emit()
        self.close()

    def clear_window(self):
        self.line_edit_note_name.clear()
        self.line_edit_note.clear()
        # self.lbl_wrong_input.setText("")
