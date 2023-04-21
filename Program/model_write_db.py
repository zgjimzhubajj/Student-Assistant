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

    def insert_student_info(self, first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program):
        print('we are now in writer class')
        self.open_db()
        self.mycursor.execute(f"SELECT program_id From program_ab_es where program_name = '{name_of_program}';")
        self.myresult = self.mycursor.fetchall()
        print(self.myresult)

        # change myResults from a list of tuples to a list of strings
        string_list = []
        for item in self.myresult:
            string_list.append(str(item[0]))
        program_id = string_list[0]
        print(program_id)

        # another way to insert
        # self.mycursor.execute(f"INSERT INTO student_info (personal_id, first_name, last_name, user_name, password, program_id, year_of_study, email) Values('{personal_id}', '{first_name}', '{last_name}', '{username}', '{password}', '{program_id}', '{year_of_study}', '{email}')")

        # Create the SQL query to insert the data
        sql = "INSERT INTO student_info (personal_id, first_name, last_name, user_name, password, program_id, year_of_study, email) Values(%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (str(personal_id), first_name, last_name, username, password, program_id, str(year_of_study), email)
        print(str(personal_id), first_name, last_name, username, password, program_id, str(year_of_study), email)

        # Execute the query and commit the changes to the database
        self.mycursor.execute(sql, val)

        # commit the changes to the database
        self.mydb.commit()

        # Print a confirmation message
        # print(self.mycursor.rowcount, "record inserted.")

        self.close_db()
