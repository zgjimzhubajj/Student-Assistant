from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from gui_create_session_window import UI_create_session_window
from gui_see_session_window import UI_see_session_window
from controller import Controller
import datetime


class UI_main_window(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None, username=None):
        super(UI_main_window, self).__init__(parent)
        uic.loadUi("gui_main_window.ui", self)
        self.username = username
        self.cntrl = Controller()

    # buttons objects
        # team session tab
        self.btn_log_out = self.findChild(QPushButton, "btn_log_out")
        self.btn_ts_create_session = self.findChild(QPushButton, "btn_ts_create_session")
        self.btn_ts_see_session = self.findChild(QPushButton, "btn_ts_see_session")
        # time manegement tab

        self.btn_tm_add_activity = self.findChild(QPushButton, "btn_tm_add_activity")
        self.btn_tm_remove_activity = self.findChild(QPushButton, "btn_tm_remove_activity")


        # material tab

    # buttons actions
        # team session tab
        self.btn_log_out.clicked.connect(self.button_log_out_pushed)
        self.btn_ts_create_session.clicked.connect(self.button_ts_create_session_pushed)
        self.btn_ts_see_session.clicked.connect(self.button_ts_see_session_pushed)

        # Time management tab

        self.btn_tm_add_activity.clicked.connect(self.open_time_schedule_dialog)
        self.btn_tm_remove_activity.clicked.connect(self.remove_activity_from_time_schedule)

        # material tab

    # label objects
        # team session tab
        self.lbl_ts_time_left_for_next_homework_1 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_1")
        self.lbl_ts_time_left_for_next_homework_2 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_2")
        self.lbl_ts_time_left_for_next_homework_3 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_3")
        self.lbl_ts_time_left_for_next_homework_4 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_4")
        self.lbl_ts_time_left_for_next_homework_5 = self.findChild(QLabel, "lbl_ts_time_left_for_next_homework_5")
        # Time management tab
        self.lbl_tm_welcome = self.findChild(QLabel, "lbl_tm_welcome")

        self.lbl_tm_reminder_message = self.findChild(QLabel, "lbl_tm_reminder_message")
        self.lbl_tm_reminder_course = self.findChild(QLabel, "lbl_tm_reminder_course")
        self.lbl_tm_reminder_task = self.findChild(QLabel, "lbl_tm_reminder_task")
        self.lbl_tm_reminder_date = self.findChild(QLabel, "lbl_tm_reminder_date")


        # material tab

    # list objects
        # team session tab
        self.list_widget_ts_homework = self.findChild(QListWidget, "list_widget_ts_homework")
        self.list_widget_homework_detail = self.findChild(QListWidget, "list_widget_homework_detail")
        # time management tab
        self.list_widget_tm_time_schedule = self.findChild(QListWidget, "list_widget_tm_time_schedule")

        # material tab

    # window settings when window open
        # team session tab
        self.list_widget_ts_homework.addItems(self.cntrl.get_course(username))
        self.list_widget_homework_detail.clear()
        # time manegement tab

        self.lbl_tm_welcome.setText(f"Welcome {self.cntrl.get_first_name(self.username).capitalize()}!\nHow would you like to organize your day?")
        self.lbl_tm_welcome.adjustSize()

        self.reminder_of_upcoming_homeworks()
        self.lbl_tm_reminder_message.adjustSize()


        # material tab

    # actions for list widget objects
        # team session tab
        self.list_widget_ts_homework.itemClicked.connect(self.text_clicked_item_homeworks)

        # time manegement tab

        # material tab

# methods for buttons action
    # team session tab
    def button_log_out_pushed(self):
        self.clear_window()
        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window

    def button_ts_create_session_pushed(self):
        self.clear_window()
        self.create_session_window = UI_create_session_window(self)
        self.create_session_window.closed.connect(self.show_this_window)
        self.close()
        self.create_session_window.show()

    def button_ts_see_session_pushed(self):
        self.clear_window()
        self.see_session_window = UI_see_session_window(self)
        self.see_session_window.closed.connect(self.show_this_window)
        self.close()
        self.see_session_window.show()

    # time manegement tab

    # material tab

# methods for list widget actions
    # team session tab
    def text_clicked_item_homeworks(self, item):
        self.list_widget_homework_detail.clear()
        course_name = item.text()
        homework_list = self.cntrl.get_homework_detail(course_name)
        for homework in homework_list:
            homework_details = "Homework name: " + homework[0] + " " + " Homework deadline: " + homework[1] + "/" + homework[2] + "/" + homework[3]
            self.list_widget_homework_detail.addItem(homework_details)

    # Time management tab

    def add_activity_to_time_schedule(self, item_text):
        self.list_widget_tm_time_schedule.addItem(item_text)

    def remove_activity_from_time_schedule(self):
        selected_items = self.list_widget_tm_time_schedule.selectedItems()
        if not selected_items:
            return

        for item in selected_items:
            self.list_widget_tm_time_schedule.takeItem(self.list_widget_tm_time_schedule.row(item))

    # material tab

# methods for main window
    def show_this_window(self):
        self.show()

    def clear_window(self):
        self.lbl_ts_time_left_for_next_homework_1.setText("")
        self.lbl_ts_time_left_for_next_homework_2.setText("")
        self.lbl_ts_time_left_for_next_homework_3.setText("")
        self.lbl_ts_time_left_for_next_homework_4.setText("")
        self.lbl_ts_time_left_for_next_homework_5.setText("")
        self.list_widget_homework_detail.clear()

    def reminder_of_upcoming_homeworks(self):
        """
        Update the labels displaying the upcoming homeworks for the logged-in user.

        Only showing those due in 14 days or less. Uses a QTimer to refresh the labels
        once every minute.
        """
        upcoming_homeworks = self.cntrl.get_homeworks(self.username)
        course = []
        task = []
        date = []
        for homework in upcoming_homeworks:
            data = homework.split(" ")
            due_date = datetime.datetime.strptime(data[2], '%Y-%m-%d').date()
            days_until_due = (due_date - datetime.date.today()).days
            if days_until_due <= 14:
                course.append(data[0])
                task.append(data[1])
                date.append(data[2])

        string_course = "\n".join(course)
        string_task = "\n".join(task)
        string_date = "\n".join(date)

        self.lbl_tm_reminder_course.setText(f"{string_course}")
        self.lbl_tm_reminder_task.setText(f"{string_task}")
        self.lbl_tm_reminder_date.setText(f"{string_date}")

        self.lbl_tm_reminder_course.adjustSize()
        self.lbl_tm_reminder_task.adjustSize()
        self.lbl_tm_reminder_date.adjustSize()

        # Create a QTimer to update the labels every minute
        timer = QTimer(self)
        timer.timeout.connect(self.reminder_of_upcoming_homeworks)
        timer.start(60000)  # 60000 milliseconds = 1 minute

    def open_time_schedule_dialog(self):
        """
        Open a dialog window to allow the user to add a new activity to the schedule.

        The dialog window contains line edit fields for the start time, end time, and activity,
        as well as "OK" and "Close" buttons. If the user clicks "OK", the new activity is added
        to the list widget. If the user clicks "Close", the dialog window is hidden and control
        returns to the main window.
        """
        dialog = QDialog()
        dialog.setWindowTitle("Add Activity")

        # Create line edit fields for start time, end time, and activity
        start_time_label = QLabel("Start time:", dialog)
        start_time_edit = QLineEdit(dialog)
        end_time_label = QLabel("End time:", dialog)
        end_time_edit = QLineEdit(dialog)
        activity_label = QLabel("Activity:", dialog)
        activity_edit = QLineEdit(dialog)
        # Create "OK" and "Cancel" buttons
        ok_button = QPushButton("OK", dialog)
        close_button = QPushButton("Close", dialog)

        # Add the line edit fields and buttons to the dialog layout
        layout = QVBoxLayout()
        layout.addWidget(start_time_label)
        layout.addWidget(start_time_edit)
        layout.addWidget(end_time_label)
        layout.addWidget(end_time_edit)
        layout.addWidget(activity_label)
        layout.addWidget(activity_edit)
        layout.addWidget(ok_button)
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        # Connect the "OK" and "Close" buttons to their respective methods
        ok_button.clicked.connect(lambda: self.add_activity_to_time_schedule(f"{start_time_edit.text()} - {end_time_edit.text()}: {activity_edit.text()}"))
        close_button.clicked.connect(dialog.hide)

        # Show the dialog and wait for the user to close it
        if dialog.exec_() == QDialog.Accepted:
            # If the user clicked "OK", add the new activity to the list widget
            start_time = start_time_edit.text()
            end_time = end_time_edit.text()
            activity = activity_edit.text()
            item_text = f"{start_time} - {end_time}: {activity}"
            self.list_widget_tm_time_schedule.addItem(item_text)
        else:
            pass
