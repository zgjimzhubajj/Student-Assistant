import mysql.connector


class Write_db():

    def __init__(self):
        pass

    def open_db(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="student_assistant"
            )
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.mycursor = self.mydb.cursor()

    def close_db(self):
        self.mycursor.close()
        self.mydb.close()

# gui_register methods
    def insert_student_info(self, first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program):
        self.open_db()
        self.mycursor.execute(f"SELECT program_id From program_ab_es where program_name = '{name_of_program}';")
        self.myresult = self.mycursor.fetchall()
        string_list = []
        for item in self.myresult:
            string_list.append(str(item[0]))
        program_id = string_list[0]

        self.mycursor.execute(f"SELECT course_id From course_ab_es where program_id = '{program_id}';")
        self.myresult = self.mycursor.fetchall()
        course_id_list = []
        for item in self.myresult:
            course_id_list.append(str(item[0]))

        self.mycursor.execute(f"INSERT INTO student_info (personal_id, first_name, last_name, user_name, password, program_name, year_of_study, email) Values('{personal_id}', '{first_name}', '{last_name}', '{username}', '{password}', '{name_of_program}', '{year_of_study}', '{email}')")
        self.mydb.commit()
        for course_id in course_id_list:
            self.mycursor.execute(f"INSERT INTO student_course_ab_es (personal_id, course_id) Values({personal_id}, {course_id})")
            # commit the changes to the database
            self.mydb.commit()
        self.close_db()

# gui_main_window methods
    # team_session tab methods
    ####################not tested yet
    def store_session(self, session_name, user_name):
        self.open_db()
        self.mycursor.execute(f"SELECT personal_id From student_info where user_name = '{user_name}';")
        self.myresult = self.mycursor.fetchall()
        personal_id_list = []
        for item in self.myresult:
            personal_id_list.append(str(item[0]))
        self.mycursor.execute(f"INSERT INTO session_ab_es (session_name, personal_id) Values('{session_name}', '{personal_id_list[0]}')")
        self.mydb.commit()
        self.close_db()

####################not tested yet
    def store_students_in_session(self, student_session_list, session_id):
        self.open_db()
        for tuple in student_session_list:
            self.mycursor.execute(f"INSERT INTO student_session_ab_es (session_id, personal_id) Values('{session_id[0]}', '{tuple[1]}')")
            self.mydb.commit()
        self.close_db()

    # time_manegment tab methods

    # material tab methods
    def add_new_note_to_db(self, note_name, note_data, username):
        self.open_db()
        self.mycursor.execute(f"SELECT personal_id From student_info Where user_name = '{username}';")
        self.myresult = self.mycursor.fetchall()
        personal_id_list = []
        for item in self.myresult:
            personal_id_list.append(item[0])
        self.mycursor.execute(f"INSERT INTO notes_mil (note_name, note_data, personal_id) Values('{note_name}', '{note_data}', {personal_id_list[0]})")
        self.mydb.commit()
        self.close_db()

################## not tested yet
    def mark_homework_as_done(self, homework_id, user_name):
        self.open_db()
        self.mycursor.execute(f"SELECT personal_id From student_info Where user_name = '{user_name}';")
        self.myresult = self.mycursor.fetchall()
        personal_id_list = []
        for item in self.myresult:
            personal_id_list.append(item[0])
        self.mycursor.execute(f"INSERT INTO finished_homework_ab_es (homework_stat, personal_id, homework_id) Values('{1}', '{personal_id_list[0]}', {homework_id})")
        self.mydb.commit()
        self.close_db()
