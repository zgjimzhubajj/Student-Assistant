import mysql.connector


class Read_db:
    def __init__(self):
        pass

    def open_db(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="student_assistant",
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
    def get_programs_names(self) -> list:
        self.open_db()
        self.mycursor.execute("SELECT program_name From program_ab_es;")
        self.myresult = self.mycursor.fetchall()
        # change myResults from a list of tuples to a list of strings
        string_list = []
        for item in self.myresult:
            string_list.append(str(item[0]))
        self.close_db()
        return string_list

    def check_user_name_exists(self, username):
        self.open_db()
        self.mycursor.execute(f"SELECT user_name From student_info Where user_name = '{username}';")
        self.myresult = self.mycursor.fetchall()
        username_list = []
        for item in self.myresult:
            username_list.append(str(item[0]))
        self.close_db()
        if username_list != []:
            return True
        else:
            return False

    # def check_personal_id_exists(self, personal_id):
    #     self.open_db()
    #     self.mycursor.execute(f"SELECT personal_id From student_info Where personal_id = '{personal_id}';")
    #     self.myresult = self.mycursor.fetchall()
    #     personal_id_list = []
    #     for item in self.myresult:
    #         personal_id_list.append(str(item[0]))
    #     self.close_db()
    #     if personal_id_list != []:
    #         return personal_id_list[0]

# gui_forgot_password methods
    def retrieve_password(self, first_name, last_name, email, username, personal_id, year_of_study, name_of_program):
        self.open_db()
        # self.mycursor.execute(f"SELECT program_id From program_ab_es where program_name = '{name_of_program}';")
        # self.myresult = self.mycursor.fetchall()
        # # change myResults from a list of tuples to a list of strings
        # string_list = []
        # for item in self.myresult:
        #     string_list.append(str(item[0]))
        # program_id = string_list[0]
        self.mycursor.execute(f"SELECT password FROM student_info WHERE personal_id = '{personal_id}' And first_name = '{first_name}' And last_name = '{last_name}' And user_name = '{username}' And email = '{email}' And year_of_study = '{year_of_study}' And program_name = '{name_of_program}';")
        self.myresult = self.mycursor.fetchall()
        password_list = []
        for item in self.myresult:
            password_list.append(str(item[0]))
        password = password_list[0]
        self.close_db()
        return password

# gui_login methods
    def check_login_stats(self, username, password):
        self.open_db()
        self.mycursor.execute(f"SELECT * FROM student_info WHERE user_name = '{username}' AND password = '{password}';")
        self.myresult = self.mycursor.fetchall()
        if self.myresult != []:
            self.close_db()
            return True
        else:
            self.close_db()
            return False

# gui_main_window methods
    # team_session tab methods

    # time_manegment tab methods

    # material tab methods
