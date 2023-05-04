from PyQt5.QtWidgets import QMainWindow, QPushButton, QComboBox, QListWidget, QSpinBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal


class UI_pomodoro_settings(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(UI_pomodoro_settings, self).__init__(parent)
        uic.loadUi("gui_pomodoro_settings.ui", self)

        # buttons object
        self.btn_cancel = self.findChild(QPushButton, "btn_cancel")
        self.btn_save = self.findChild(QPushButton, "btn_save")

        # buttons actions
        self.btn_cancel.clicked.connect(self.button_cancel_pushed)
        self.btn_save.clicked.connect(self.button_save_pushed)

        # comboBox object
        self.combo_box_type_of_pomodoro = self.findChild(QComboBox, "combo_box_type_of_pomodoro")
        self.combo_box_type_of_media = self.findChild(QComboBox, "combo_box_type_of_media")

        # list widget object
        self.list_widget_name_of_media = self.findChild(QListWidget, "list_widget_name_of_media")

        # spinBox object
        self.spin_box_number_of_sessions = self.findChild(QSpinBox, "spin_box_number_of_sessions")

    def button_cancel_pushed(self):
        self.clear_window()
        self.closed.emit()
        self.close()

    def button_save_pushed(self):
        self.clear_window()
        self.closed.emit()
        self.close()

    def clear_window(self):
        self.combo_box_type_of_pomodoro.setCurrentIndex(-1)
        self.combo_box_type_of_media.setCurrentIndex(-1)
        self.list_widget_name_of_media.clear()
        self.spin_box_number_of_sessions.setValue(0)
