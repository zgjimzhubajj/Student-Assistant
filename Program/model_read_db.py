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
