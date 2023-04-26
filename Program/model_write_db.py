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
        # self.mycursor.execute(f"SELECT program_id From program_ab_es where program_name = '{name_of_program}';")
        # self.myresult = self.mycursor.fetchall()
        # # change myResults from a list of tuples to a list of strings
        # string_list = []
        # for item in self.myresult:
        #     string_list.append(str(item[0]))
        # program_id = string_list[0]
        self.mycursor.execute(f"INSERT INTO student_info (personal_id, first_name, last_name, user_name, password, program_name, year_of_study, email) Values('{personal_id}', '{first_name}', '{last_name}', '{username}', '{password}', '{name_of_program}', '{year_of_study}', '{email}')")
        # commit the changes to the database
        self.mydb.commit()
        self.close_db()

# gui_main_window methods
    # team_session tab methods

    # time_manegment tab methods

    # material tab methods
