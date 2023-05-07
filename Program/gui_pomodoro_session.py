from PyQt5.QtWidgets import QMainWindow, QPushButton, QComboBox, QListWidget, QLabel,QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap


class UI_pomodoro_session(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None, type_of_pomodoro = None, number_of_sessions = None):
        super(UI_pomodoro_session, self).__init__(parent)
        uic.loadUi("gui_pomodoro_session.ui", self)
        self.type_of_pomodoro = type_of_pomodoro
        self.number_of_sessions = number_of_sessions
        self.is_break = False

        # buttons object
        self.btn_end_session = self.findChild(QPushButton, "btn_end_session")

        # buttons actions
        self.btn_end_session.clicked.connect(self.button_end_session_pushed)

        # Set up the timer with a 1-second interval
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)
        
        # Start the timer
        self.remaining_time = 30 if self.type_of_pomodoro == 2 else 15 # 50 or 25 minutes in seconds
        self.timer.start()

        # Add an image to the GUI
        if self.type_of_pomodoro == 1:
            pixmap = QPixmap('study.png')
            self.lbl_image.setPixmap(pixmap)
        else:
            pixmap = QPixmap('studies.png')
            self.lbl_image.setPixmap(pixmap)

        # label objects
        self.lbl_study_break_condition = self.findChild(QLabel, "lbl_study_break_condition")
        self.lbl_backwards_counter = self.findChild(QLabel, "lbl_backwards_counter")
        self.lbl_image = self.findChild(QLabel, 'lbl_image')

    def button_end_session_pushed(self):
        self.parent().btn_tm_start_pomodoro.setEnabled(False)
        self.clear_window()
        self.closed.emit()
        self.close()

    def update_timer(self):
        # Decrement the remaining time
        self.remaining_time -= 1
        
        # Convert the remaining time to minutes and seconds
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        
        # Update the text of the label with the current remaining time
        self.lbl_backwards_counter.setText(f"{minutes:02d}:{seconds:02d}")
        
        # Show a popup message when it's time for a break
        if self.remaining_time == 0:
            QMessageBox.information(self, "Break Time", "It's time for a break!")
            self.remaining_time = 6 if self.type_of_pomodoro == 2 else 3 # 10 or 5 minutes in seconds
            self.lbl_backwards_counter.setText("10:00" if self.type_of_pomodoro == 2 else "05:00")
            
            # Start and the timer for the break
            self.timer.start()

    def clear_window(self):
        self.lbl_study_break_condition.setText("")
        self.lbl_backwards_counter.setText("")
