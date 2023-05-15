from model_read_db import Read_db
from model_write_db import Write_db
from model_open_pdf import Open_pdf

class Controller():
    def __init__(self):
        self.read_db = Read_db()
        self.write_db = Write_db()
        self.open_pdf = Open_pdf()

# gui_register window methods
    def get_programs_info_from_database(self): # to fill the combo box
        program_names_list = self.read_db.get_programs_names()
        program_names_list.insert(0, "")
        return program_names_list

    def register_student_in_database(self, first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program):
        self.write_db.insert_student_info(first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program)

    def check_user_name_exists(self, username):
        if self.read_db.check_user_name_exists(username):
            return True
        else:
            return False

    def check_personal_id_exists(self, personal_id):
        personal_id = self.read_db.check_personal_id_exists(personal_id)
        return personal_id

# gui_login window methods
    def check_login_stats(self, username, password):
        if self.read_db.check_login_stats(username, password):
            return True
        else:
            return False

# gui_forgot_password methods
    def retrieve_password(self, first_name, last_name, email, username, personal_id, year_of_study, name_of_program):
        self.password = self.read_db.retrieve_password(first_name, last_name, email, username, personal_id, year_of_study, name_of_program)
        return self.password

    def check_user_exists(self, first_name, last_name, email, username, name_of_program, personal_id, year_of_study):
        return self.read_db.check_user_exists(first_name, last_name, email, username, name_of_program, personal_id, year_of_study)

# gui_main_window methods
    # time_management tab methods
    def get_first_name(self, username):
        return self.read_db.get_first_name(username)

    def get_homeworks(self, username):
        return self.read_db.get_homeworks(username)

    # team_session tab methods
    def get_course(self, username):
        return self.read_db.get_course(username)

    def get_homework_detail(self, course_name):
        return self.read_db.get_homework_detail(course_name)

    def get_students(self, user_name):
        student_list = self.read_db.get_students(user_name)
        tuple = ("", 0)
        student_list.insert(0, tuple)
        return student_list

    def get_first_name_last_name(self, user_name):
        return self.read_db.get_first_name_last_name(user_name)

    def check_session_name(self, session_name, user_name):
        return self.read_db.check_session_name(session_name, user_name)
    
    def check_session_members(self, student_session_list, user_name):
        return self.read_db.check_session_members(student_session_list, user_name)
    
    def store_session(self, session_name, user_name):
        self.write_db.store_session(session_name, user_name)

    def get_session_id(self, session_name, user_name):
        return self.read_db.get_session_id(session_name, user_name)

    def store_students_in_session(self, student_session_list, session_id):
        self.write_db.store_students_in_session(student_session_list, session_id)

    # material tab methods
    def get_lecture_detail(self, course_name):
        return self.read_db.get_lecture_detail(course_name)

    def get_lecture(self, course_name_m_course, lecture_name):
        return self.read_db.get_lecture(course_name_m_course, lecture_name)

    def open_lecture(self, lecture_record):
        self.open_pdf.open_lecture(lecture_record)

    def get_notes(self, username):
        return self.read_db.get_notes(username)

    def add_new_note_to_db(self, note_name, note_data, username):
        self.write_db.add_new_note_to_db(note_name, note_data, username)

    def check_if_note_name_exist(self, note_name, username):
        return self.read_db.check_if_note_name_exist(note_name, username)

    def get_note_data(self, note_name, username):
        return self.read_db.get_note_data(note_name, username)
