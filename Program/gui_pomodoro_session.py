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
        self.number_of_sessions1 = self.number_of_sessions

        self.btn_end_session = self.findChild(QPushButton, "btn_end_session")

        self.btn_end_session.clicked.connect(self.button_end_session_pushed)

        # Add an image to the GUI
        if self.type_of_pomodoro == 1:
            pixmap = QPixmap('study.png')
            self.lbl_image.setPixmap(pixmap)
        else:
            pixmap = QPixmap('studies.png')
            self.lbl_image.setPixmap(pixmap)

        # label objects
        self.lbl_backwards_counter = self.findChild(QLabel, "lbl_backwards_counter")
        self.lbl_number_of_sessoins = self.findChild(QLabel, "lbl_number_of_sessoins")
        self.lbl_image = self.findChild(QLabel, 'lbl_image')

        # Set up the timer with a 1-second interval
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        # Set initial values for the countdown and loops
        self.remaining_time = 1500 if self.type_of_pomodoro == 1 else 3000
        self.is_break = False
        self.loop_count = 0

        # Start the timer
        self.timer.start()

    def update_timer(self):
        self.lbl_number_of_sessoins.setText(f"Sessions you have left: {self.number_of_sessions1}")
        # Decrement the remaining time
        self.remaining_time -= 1

        # Convert the remaining time to minutes and seconds
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60

        # Update the text of the label with the current remaining time
        self.lbl_backwards_counter.setText(f"{minutes:02d}:{seconds:02d}")

        # Check if the countdown has reached 0
        if self.remaining_time == 0:
            # Toggle the is_break flag and reset the remaining time
            self.is_break = not self.is_break
            if self.is_break:
                self.remaining_time = 300 if self.type_of_pomodoro == 1 else 600
                QMessageBox.information(self, "Break Time", "It's time for a break")
            else:
                self.remaining_time = 1500 if self.type_of_pomodoro == 1 else 3000

            # Increment the loop count if it's not a break
            if not self.is_break:
                self.loop_count += 1
                self.number_of_sessions1 = self.number_of_sessions1 - self.loop_count

            # Stop the timer if the loop count reached 2
            if self.loop_count == self.number_of_sessions:
                self.timer.stop()
                QMessageBox.information(self, "Session ended", "Please press end session button to go back to main window")


    def button_end_session_pushed(self):
        self.timer.stop()
        self.parent().btn_tm_start_pomodoro.setEnabled(False)
        self.clear_window()
        self.closed.emit()
        self.close()

    def clear_window(self):
        self.lbl_backwards_counter.setText("")
