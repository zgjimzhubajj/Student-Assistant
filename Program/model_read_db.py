import mysql.connector


class Read_db():

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

    def check_user_name_exist(self, username):
        self.open_db()

        self.mycursor.execute(f"SELECT user_name FROM student_info WHERE user_name = '{username}'")

        self.myresult = self.mycursor.fetchall()
        if self.myresult != []:
            self.close_db()
            return True
        else:
            self.close_db()
            return False

# gui_forgot_password methods

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
