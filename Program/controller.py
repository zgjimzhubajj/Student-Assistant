from model_read_db import Read_db
from model_write_db import Write_db


class Controller():
    def __init__(self):
        self.read_db = Read_db()
        self.write_db = Write_db()

    def get_programs_info_from_database(self):
        program_names_list = self.read_db.get_programs_names()
        program_names_list.insert(0, "")
        return program_names_list

    def register_student_in_database(self, first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program):
        self.write_db.insert_student_info(first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program)
