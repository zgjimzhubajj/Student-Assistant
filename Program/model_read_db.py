import mysql.connector
import datetime


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

    def check_personal_id_exists(self, personal_id):
        self.open_db()
        self.mycursor.execute(f"SELECT personal_id From student_info Where personal_id = '{personal_id}';")
        self.myresult = self.mycursor.fetchall()
        personal_id_list = []
        for item in self.myresult:
            personal_id_list.append(str(item[0]))
        self.close_db()
        if personal_id_list != []:
            return True
        else:
            return False

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

    def check_user_exists(self, first_name, last_name, email, username, name_of_program, personal_id, year_of_study):
        self.open_db()
        self.mycursor.execute(f"SELECT * From student_info Where first_name = '{first_name}' and last_name = '{last_name}' and email = '{email}' and user_name = '{username}' and program_name = '{name_of_program}' and year_of_study = '{year_of_study}' and personal_id = '{personal_id}';")
        self.myresult = self.mycursor.fetchall()
        user_list = []
        for item in self.myresult:
            user_list.append(str(item[0]))
        self.close_db()
        if user_list != []:
            return True
        else:
            return False

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
    def get_course(self, username):
        self.open_db()
        self.mycursor.execute(f"SELECT year_of_study From student_info where user_name = '{username}';")
        self.myresult = self.mycursor.fetchall()
        year_of_study = []
        for item in self.myresult:
            year_of_study.append(str(item[0]))
        year_of_study_of_student = year_of_study[0]
        self.mycursor.execute(f"SELECT course_name FROM student_info JOIN student_course_ab_es ON student_info.personal_id = student_course_ab_es.personal_id JOIN course_ab_es ON student_course_ab_es.course_id = course_ab_es.course_id where student_info.user_name = '{username}' and course_ab_es.course_year = {year_of_study_of_student};")
        self.myresult = self.mycursor.fetchall()
        course_list = []
        for item in self.myresult:
            course_list.append(str(item[0]))
        self.close_db()
        return course_list

    def get_homework_detail(self, course_name):
        self.open_db()
        self.mycursor.execute(f"select course_id from course_ab_es where course_name = '{course_name}';")
        self.myresult = self.mycursor.fetchall()
        course_list = []
        for item in self.myresult:
            course_list.append(str(item[0]))
        course_id = course_list[0]
        self.mycursor.execute(f"select homework_name, homework_dead_line from homework_ab_es where course_id = {course_id};")
        self.myresult = self.mycursor.fetchall()
        list_of_lists = []
        for tup in self.myresult:
            # Extract the relevant values from the tuple
            str_val = tup[0]
            year_val = str(tup[1].year)
            month_val = str(tup[1].month)
            day_val = str(tup[1].day)
            # Create a new list with the extracted values
            new_list = [str_val, year_val, month_val, day_val]
            # Append the new list to the list of lists
            list_of_lists.append(new_list)
        self.close_db()
        return list_of_lists

    # Time_management tab methods
    def get_first_name(self, username):
        self.open_db()
        self.mycursor.execute(f"SELECT first_name FROM student_info WHERE user_name = '{username}';")
        self.myresult = self.mycursor.fetchall()
        list_of_first_name = []
        for item in self.myresult:
            list_of_first_name.append(item[0])
        self.close_db()
        return list_of_first_name[0]

    def get_homeworks(self, username):
        list_courses = self.get_course(username)
        list_of_homeworks = []
        for course in list_courses:
            line_in_example_list = f"{course}"
            for homework in self.get_homework_detail(course):
                line_in_example_list = line_in_example_list + " " + homework[0] + " " + homework[1] + "-" + homework[2] + "-" + homework[3]
                list_of_homeworks.append(line_in_example_list)
        return list_of_homeworks
    # not tested yet#############
    def get_media_type_from_database(self):
        self.open_db()
        self.mycursor.execute("SELECT media_name FROM media_type_zgj")
        self.myresult = self.mycursor.fetchall()
        list_media_type = []
        for item in self.myresult:
            list_media_type.append(item[0])
        self.close_db()
        list_media_type.insert(0, "")
        return list_media_type

    # not tested yet#############
    def get_name_of_media(self, type_of_media):
        self.open_db()
        self.mycursor.execute(f"SELECT media_id FROM media_type_zgj where media_name = '{type_of_media}';")
        self.myresult = self.mycursor.fetchall()
        list_media_id = []
        for item in self.myresult:
            list_media_id.append(str(item[0]))
        self.mycursor.execute(f"SELECT media_name FROM media_name_zgj where media_id = {list_media_id[0]};")
        self.myresult = self.mycursor.fetchall()
        list_media_name = []
        for item in self.myresult:
            list_media_name.append(item[0])
        self.close_db()  
        return list_media_name



    # material tab methods
    # not tested yet#############
    def get_lecture_detail(self, course_name):
        self.open_db()
        self.mycursor.execute(f"select course_id from course_ab_es where course_name = '{course_name}';")
        self.myresult = self.mycursor.fetchall()
        course_list = []
        for item in self.myresult:
            course_list.append(str(item[0]))
        course_id = course_list[0]
        self.mycursor.execute(f"select file_name from pdf_files_mil where course_id = {course_id};")
        self.myresult = self.mycursor.fetchall()
        list_of_lists = []
        for tup in self.myresult:
            list_of_lists.append(tup[0])
        self.close_db()
        return list_of_lists
    #not tested yet########
    def get_lecture(self, course_name_m_course, lecture_name):
        self.open_db()
        self.mycursor.execute(f"select course_id from course_ab_es where course_name = '{course_name_m_course}';")
        self.myresult = self.mycursor.fetchall()
        course_list = []
        for item in self.myresult:
            course_list.append(item[0])
        course_id = course_list[0]
        self.mycursor.execute(f"select id from pdf_files_mil where course_id = {course_id} and file_name = '{lecture_name}';")#it might show error here because i didnt serround course_id with single coutation
        self.myresult = self.mycursor.fetchall()
        id_list = []
        for item in self.myresult:
            id_list.append(str(item[0]))
        id = id_list[0]
        # Retrieve the binary data and file name from the MySQL table
        sql_query = "SELECT file_name, file_data FROM pdf_files_mil WHERE id = %s"
        self.mycursor.execute(sql_query, (id,))
        record = self.mycursor.fetchone()
        return record

    # not tested yet#############
    def get_notes(self, username):
        self.open_db()
        self.mycursor.execute(f"SELECT personal_id From student_info Where user_name = '{username}';")
        self.myresult = self.mycursor.fetchall()
        personal_id_list = []
        for item in self.myresult:
            personal_id_list.append(item[0])
        self.mycursor.execute(f"SELECT note_name From notes_mil Where personal_id = {personal_id_list[0]};")
        self.myresult = self.mycursor.fetchall()
        note_name_list = []
        for item in self.myresult:
            note_name_list.append(str(item[0]))
        self.close_db()
        return note_name_list

    # not tested yet#############
    def check_if_note_name_exist(self, note_name, username):
        self.open_db()
        self.mycursor.execute(f"SELECT personal_id From student_info Where user_name = '{username}';")
        self.myresult = self.mycursor.fetchall()
        personal_id_list = []
        for item in self.myresult:
            personal_id_list.append(item[0])

        self.mycursor.execute(f"SELECT note_name From notes_mil Where personal_id = {personal_id_list[0]};")
        self.myresult = self.mycursor.fetchall()
        note_name_list = []
        for item in self.myresult:
            note_name_list.append(str(item[0]))
        if note_name in note_name_list:
            self.close_db()
            return True
        else:
            self.close_db()
            return False
    # not tested yet#############
    def get_note_data(self, note_name, username):
        self.open_db()
        self.mycursor.execute(f"SELECT personal_id From student_info Where user_name = '{username}';")
        self.myresult = self.mycursor.fetchall()
        personal_id_list = []
        for item in self.myresult:
            personal_id_list.append(item[0])
        self.mycursor.execute(f"SELECT note_data From notes_mil Where personal_id = {personal_id_list[0]} and note_name = '{note_name}';")
        self.myresult = self.mycursor.fetchall()
        note_data_list = []
        for item in self.myresult:
            note_data_list.append(str(item[0]))
        self.close_db()
        return note_data_list[0]
