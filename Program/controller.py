from model_read_db import Read_db
from model_write_db import Write_db


class Controller():
    def __init__(self):
        self.read_db = Read_db()
        self.write_db = Write_db()

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

    # material tab methods
