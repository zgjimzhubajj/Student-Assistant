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

# gui_login window methods
    def check_login_stats(self, username, password):
        if self.read_db.check_login_stats(username, password):
            return True
        else:
            return False

# gui_main_window methods
    # tab_time_management methods

    # tab_team_session methods
