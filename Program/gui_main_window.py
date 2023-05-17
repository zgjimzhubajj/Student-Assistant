from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from gui_create_session_window import UI_create_session_window
from gui_see_session_window import UI_see_session_window
from gui_time_schedule_dialog import UI_dialog_window
from gui_pomodoro_settings import UI_pomodoro_settings
from gui_pomodoro_session import UI_pomodoro_session
from gui_note_window import UI_note_window
from controller import Controller
import datetime


class UI_main_window(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None, username=None):
        super(UI_main_window, self).__init__(parent)
        uic.loadUi("gui_main_window.ui", self)
        self.username = username
        self.cntrl = Controller()
        self.window_obj = self.window

    # buttons objects
        # team session tab
        self.btn_log_out = self.findChild(QPushButton, "btn_log_out")
        self.btn_ts_create_session = self.findChild(QPushButton, "btn_ts_create_session")
        self.btn_ts_see_session = self.findChild(QPushButton, "btn_ts_see_session")
        # time manegement tab
        self.btn_tm_add_activity = self.findChild(QPushButton, "btn_tm_add_activity")
        self.btn_tm_remove_activity = self.findChild(QPushButton, "btn_tm_remove_activity")
        self.btn_tm_start_pomodoro = self.findChild(QPushButton, "btn_tm_start_pomodoro")
        self.btn_tm_pomodoro_settings = self.findChild(QPushButton, "btn_tm_pomodoro_settings")
        # material tab
        self.btn_m_select_lecture = self.findChild(QPushButton, "btn_m_select_lecture")
        self.btn_m_add_note = self.findChild(QPushButton, "btn_m_add_note")

    # buttons actions
        # team session tab
        self.btn_log_out.clicked.connect(self.button_log_out_pushed)
        self.btn_ts_create_session.clicked.connect(self.button_ts_create_session_pushed)
        self.btn_ts_see_session.clicked.connect(self.button_ts_see_session_pushed)
        # Time management tab
        self.btn_tm_add_activity.clicked.connect(self.btn_tm_add_activity_pushed)
        self.btn_tm_remove_activity.clicked.connect(self.btn_tm_remove_activity_pushed)
        self.btn_tm_start_pomodoro.clicked.connect(self.btn_tm_start_pomodoro_pushed)
        self.btn_tm_pomodoro_settings.clicked.connect(self.btn_tm_pomodoro_settings_pushed)
        # material tab
        self.btn_m_select_lecture.clicked.connect(self.btn_m_select_lecture_pushed)
        self.btn_m_add_note.clicked.connect(self.btn_m_add_note_pushed)

    # label objects
        # Time management tab
        self.lbl_tm_welcome = self.findChild(QLabel, "lbl_tm_welcome")
        self.lbl_tm_reminder_message = self.findChild(QLabel, "lbl_tm_reminder_message")
        self.lbl_tm_reminder_course = self.findChild(QLabel, "lbl_tm_reminder_course")
        self.lbl_tm_reminder_task = self.findChild(QLabel, "lbl_tm_reminder_task")
        self.lbl_tm_reminder_date = self.findChild(QLabel, "lbl_tm_reminder_date")
        # material tab
        self.lbl_m_note_text = self.findChild(QLabel, "lbl_m_note_text")

    # list objects
        # team session tab
        self.list_widget_ts_courses = self.findChild(QListWidget, "list_widget_ts_courses")
        self.list_widget_homework_detail = self.findChild(QListWidget, "list_widget_homework_detail")
        # time management tab
        self.list_widget_tm_time_schedule = self.findChild(QListWidget, "list_widget_tm_time_schedule")
        # material tab
        self.list_widget_m_courses = self.findChild(QListWidget, "list_widget_m_courses")
        self.list_widget_m_lectures = self.findChild(QListWidget, "list_widget_m_lectures")
        self.list_widget_m_notes = self.findChild(QListWidget, "list_widget_m_notes")

    # window settings when window open
        # team session tab
        self.list_widget_ts_courses.addItems(self.cntrl.get_course(username))
        self.list_widget_homework_detail.clear()
        # time manegement tab
        self.lbl_tm_welcome.setText(f"Welcome {self.cntrl.get_first_name(self.username).capitalize()}!\nHow would you like to organize your day?")
        self.lbl_tm_welcome.adjustSize()
        self.btn_pomodoro_settings_pushed = False
        if not self.btn_pomodoro_settings_pushed:
            self.btn_tm_start_pomodoro.setEnabled(False)
        else:
            self.btn_tm_start_pomodoro.setEnabled(True)

        self.reminder_of_upcoming_homeworks()
        self.lbl_tm_reminder_message.adjustSize()
        # material tab
        self.lbl_m_note_text.setText("")
        self.list_widget_m_courses.addItems(self.cntrl.get_course(username))
        self.list_widget_m_notes.addItems(self.cntrl.get_notes(username))
        self.course_name_m_course = ""
        self.lecture_name = ""

    # actions for list widget objects
        # team session tab
        self.list_widget_ts_courses.itemClicked.connect(self.text_clicked_item_homeworks)

        # time manegement tab

        # material tab
        self.list_widget_m_courses.itemClicked.connect(self.text_clicked_item_courses)
        self.list_widget_m_lectures.itemClicked.connect(self.text_clicked_item_lecture)
        self.list_widget_m_notes.itemClicked.connect(self.text_clicked_item_note)

# methods for buttons action
    # team session tab
    def button_log_out_pushed(self):
        self.clear_window()
        self.closed.emit()  # emit the closed signal
        self.close()  # close the new window

    def button_ts_create_session_pushed(self):
        self.clear_window()
        self.create_session_window = UI_create_session_window(self, self.username)
        self.create_session_window.closed.connect(self.show_this_window)
        self.close()
        self.create_session_window.show()

    def button_ts_see_session_pushed(self):
        self.clear_window()
        self.see_session_window = UI_see_session_window(self, self.username)
        self.see_session_window.closed.connect(self.show_this_window)
        self.close()
        self.see_session_window.show()

    # time manegement tab
    def btn_tm_add_activity_pushed(self):
        self.dialog = UI_dialog_window(self)
        self.dialog.closed.connect(self.show_this_window)
        self.close()
        self.dialog.show()

    def add_dialog(self, item_text):
        self.list_widget_tm_time_schedule.addItem(item_text)

    def btn_tm_remove_activity_pushed(self):
        selected_items = self.list_widget_tm_time_schedule.selectedItems()
        if not selected_items:
            return

        for item in selected_items:
            self.list_widget_tm_time_schedule.takeItem(self.list_widget_tm_time_schedule.row(item))

    def btn_tm_start_pomodoro_pushed(self):
        self.pomodoro_session = UI_pomodoro_session(self, self.type_of_pomodoro, self.number_of_sessions)
        self.pomodoro_session.closed.connect(self.show_this_window)
        self.close()
        self.pomodoro_session.show()

    def store_pomodoro_settings(self, type_of_pomodoro, number_of_sessions):
        self.type_of_pomodoro = type_of_pomodoro
        self.number_of_sessions = number_of_sessions

    def btn_tm_pomodoro_settings_pushed(self):
        self.pomodoro_settings = UI_pomodoro_settings(self)
        self.pomodoro_settings.closed.connect(self.show_this_window)
        self.close()
        self.pomodoro_settings.show()


    # material tab
    def btn_m_select_lecture_pushed(self):
        if self.course_name_m_course == "" or self.lecture_name == "":
            pass
        else:
            lecture_record = self.cntrl.get_lecture(self.course_name_m_course, self.lecture_name)
            self.cntrl.open_lecture(lecture_record)

    def btn_m_add_note_pushed(self):
        self.note_window = UI_note_window(self)
        self.note_window.closed.connect(self.show_this_window)
        self.close()
        self.note_window.show()

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

    # material tab
    def text_clicked_item_courses(self, item):
        self.list_widget_m_lectures.clear()
        self.course_name_m_course = item.text()
        lecture_list = self.cntrl.get_lecture_detail(self.course_name_m_course)
        for lecture in lecture_list:
            self.list_widget_m_lectures.addItem(lecture)

    def text_clicked_item_lecture(self, item):
        self.lecture_name = item.text()

    def text_clicked_item_note(self, item):
        self.lbl_m_note_text.setText(self.cntrl.get_note_data(item.text(), self.username))

# methods for main window
    def show_this_window(self):
        self.show()

    def clear_window(self):
        self.list_widget_homework_detail.clear()
        self.list_widget_tm_time_schedule.clear()
        self.btn_tm_start_pomodoro.setEnabled(False)

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
            if days_until_due <= 14 and  days_until_due >=0:
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
