from PyQt5.QtWidgets import QMainWindow, QPushButton, QComboBox, QSpinBox, QLabel
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from controller import Controller


class UI_pomodoro_settings(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(UI_pomodoro_settings, self).__init__(parent)
        uic.loadUi("gui_pomodoro_settings.ui", self)
        self.cntrl = Controller()

        # buttons object
        self.btn_cancel = self.findChild(QPushButton, "btn_cancel")
        self.btn_save = self.findChild(QPushButton, "btn_save")

        # buttons actions
        self.btn_cancel.clicked.connect(self.button_cancel_pushed)
        self.btn_save.clicked.connect(self.button_save_pushed)

        # comboBox object
        self.combo_box_type_of_pomodoro = self.findChild(QComboBox, "combo_box_type_of_pomodoro")

        # spinBox object
        self.spin_box_number_of_sessions = self.findChild(QSpinBox, "spin_box_number_of_sessions")

        # label objects
        self.lbl_wrong_inputs = self.findChild(QLabel, "lbl_wrong_inputs")
        self.lbl_wrong_inputs.setStyleSheet("color: red")

        # when window open settings for combobox and spinbox
        self.combo_box_type_of_pomodoro.addItems(self.add_pomodoro_type())

    def button_cancel_pushed(self):
        self.clear_window()
        self.closed.emit()
        self.close()

    def button_save_pushed(self):
        # Check if combo boxes are at index 0
        if self.combo_box_type_of_pomodoro.currentIndex() == 0:
            # Display error message
            self.lbl_wrong_inputs.setText("Please select a type of Pomodoro")
        elif self.spin_box_number_of_sessions.value() == 0:
            # Display error message
            self.lbl_wrong_inputs.setText("Please select how many session you want")
        else:
            self.parent().btn_tm_start_pomodoro.setEnabled(True)
            self.type_of_pomodoro = self.combo_box_type_of_pomodoro.currentIndex()
            self.number_of_sessions = self.spin_box_number_of_sessions.value()
            self.parent().store_pomodoro_settings(self.type_of_pomodoro, self.number_of_sessions)
            self.clear_window()
            self.closed.emit()
            self.close()

    def add_pomodoro_type(self):
        pomodoro_type = ["","5 min Break, 25 min Study","10 min Break, 50 min Study"]
        return pomodoro_type            

    def clear_window(self):
        self.combo_box_type_of_pomodoro.setCurrentIndex(0)
        self.spin_box_number_of_sessions.setValue(0)
        #get the lbl object put i up then add it here on clear window
