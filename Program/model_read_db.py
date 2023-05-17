import mysql.connector
import datetime
import copy


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

################ not tested yet
    def get_students(self, user_name):
        self.open_db()
        self.mycursor.execute(f"select program_name, year_of_study from student_info where user_name = '{user_name}';")
        self.myresult = self.mycursor.fetchall()
        program_year_list = []
        for item in self.myresult:
            program_year_list.append(str(item[0]))
            program_year_list.append(str(item[1]))
        program = program_year_list[0]
        year = program_year_list[1]
        self.mycursor.execute(f"select first_name, last_name, personal_id from student_info where program_name = '{program}' and year_of_study = '{year}';")
        self.myresult = self.mycursor.fetchall()
        student_list = []
        tuple = ()
        for item in self.myresult:
            student_name = item[0] + " " + item[1]
            student_personal_id = item[2]
            tuple = (student_name, student_personal_id)
            student_list.append(tuple)
        self.close_db()
        return student_list

    ################ not tested yet
    def get_first_name_last_name(self, user_name):
        self.open_db()
        self.mycursor.execute(f"select first_name, last_name from student_info where user_name = '{user_name}';")
        self.myresult = self.mycursor.fetchall()
        user_list = []
        for item in self.myresult:
            user_list.append(str(item[0]))
            user_list.append(str(item[1]))
        first_name = user_list[0]
        last_name = user_list[1]
        self.close_db()
        return first_name, last_name

################### not tested yet
    def check_session_name(self, session_name, user_name):
        self.open_db()
        self.mycursor.execute(f"SELECT personal_id From student_info where user_name = '{user_name}';")
        self.myresult = self.mycursor.fetchall()
        personal_id_list = []
        for item in self.myresult:
            personal_id_list.append(str(item[0]))
        self.mycursor.execute(f"select session_name from session_ab_es where session_name = '{session_name}' and personal_id = '{personal_id_list[0]}';")
        self.myresult = self.mycursor.fetchall()
        session_name_list = []
        for item in self.myresult:
            session_name_list.append(str(item[0]))
        self.close_db()
        if session_name_list != []:
            return True
        else:
            return False

    ###################### not tested yet
    def check_session_members(self, student_session_list, user_name):
        list_exist = False
        session_id_list = self.get_session_ids(user_name)
        if session_id_list == []:
            return False
        else:
            self.open_db()
            for session_id in session_id_list:
                self.mycursor.execute(f"SELECT personal_id From student_session_ab_es where session_id = '{session_id}';")
                self.myresult = self.mycursor.fetchall()
                personal_id_list_db = []
                for item in self.myresult:
                    personal_id_list_db.append(str(item[0]))
                personal_id_list_prog = []
                for tuple in student_session_list:
                    personal_id_list_prog.append(str(tuple[1]))
                set1 = set(personal_id_list_db)
                set2 = set(personal_id_list_prog)
                if set1 == set2:
                    self.close_db()
                    list_exist = True
                    return list_exist
                else:
                    self.close_db()
                    return list_exist

################not tested yet
    def get_session_ids(self, user_name):
        self.open_db()
        self.mycursor.execute(f"SELECT personal_id From student_info where user_name = '{user_name}';")
        self.myresult = self.mycursor.fetchall()
        personal_id_list = []
        for item in self.myresult:
            personal_id_list.append(str(item[0]))
        self.mycursor.execute(f"SELECT session_id From session_ab_es where personal_id = '{personal_id_list[0]}';")
        self.myresult = self.mycursor.fetchall()
        session_id_list = []
        for item in self.myresult:
            session_id_list.append(str(item[0]))
        self.close_db()
        if session_id_list == []:
            return []
        else:
            return session_id_list

    def get_session_id(self, session_name, user_name):
        self.open_db()
        self.mycursor.execute(f"SELECT personal_id From student_info where user_name = '{user_name}';")
        self.myresult = self.mycursor.fetchall()
        personal_id_list = []
        for item in self.myresult:
            personal_id_list.append(str(item[0]))
        self.mycursor.execute(f"SELECT session_id From session_ab_es where personal_id = '{personal_id_list[0]}' and session_name = '{session_name}';")
        self.myresult = self.mycursor.fetchall()
        session_id_list = []
        for item in self.myresult:
            session_id_list.append(str(item[0]))
        self.close_db()
        return session_id_list
        # if session_id_list == []:
        #     return []
        # else:
        #     return session_id_list

    ######### not tested yet
    def get_sessions_names(self, user_name):
        self.open_db()
        self.mycursor.execute(f"SELECT personal_id From student_info where user_name = '{user_name}';")
        self.myresult = self.mycursor.fetchall()
        personal_id_list = []
        for item in self.myresult:
            personal_id_list.append(str(item[0]))
        self.mycursor.execute(f"SELECT session_name From session_ab_es where personal_id = '{personal_id_list[0]}';")
        self.myresult = self.mycursor.fetchall()
        session_name_list = []
        for item in self.myresult:
            session_name_list.append(str(item[0]))
        self.close_db()
        return session_name_list

    ########### not tested yet
    def get_homeworks_names(self, user_name):
        self.open_db()
        self.mycursor.execute(f"SELECT homework_ab_es.homework_name, homework_ab_es.homework_id, homework_ab_es.course_id FROM student_info JOIN student_course_ab_es ON student_info.personal_id = student_course_ab_es.personal_id JOIN course_ab_es ON student_course_ab_es.course_id = course_ab_es.course_id JOIN homework_ab_es ON course_ab_es.course_id = homework_ab_es.course_id WHERE student_info.user_name = '{user_name[0]}';")
        self.myresult = self.mycursor.fetchall()
        self.close_db()
        return self.myresult

    ######### not tested yet
    def get_students_session(self, session_name, user_name):
        session_id_list = self.get_session_id(session_name, user_name)
        self.open_db()
        session_id = session_id_list[0]
        self.mycursor.execute(f"SELECT personal_id From student_session_ab_es where session_id = '{session_id}';")
        self.myresult = self.mycursor.fetchall()
        student_id_list = []
        for item in self.myresult:
            student_id_list.append(str(item[0]))
        student_name_list = []
        for id in student_id_list:
            self.mycursor.execute(f"SELECT first_name, last_name, personal_id From student_info where personal_id = '{id}';")
            self.myresult = self.mycursor.fetchall()
            for tuple in self.myresult:
                first_name = tuple[0]
                last_name = tuple[1]
                personal_id = tuple[2]
                name = first_name + " " + last_name
                student_name_list.append((name, personal_id))
        self.close_db()
        return student_name_list

    ############# not tested yet
    def check_if_homework_finished(self, homeworks_tuple_list, personal_id):
        homeworks_tuple_list_new = homeworks_tuple_list
        self.open_db()
        self.mycursor.execute(f"SELECT homework_id From finished_homework_ab_es where personal_id = '{personal_id}';")
        self.myresult = self.mycursor.fetchall()
        index_list_of_deletion = []
        homework_id_list = []
        for item in self.myresult:
            homework_id_list.append(item[0])
        for index, tuple in enumerate(homeworks_tuple_list_new):
            for homework_id in homework_id_list:
                if homework_id == tuple[1]:
                    index_list_of_deletion.append(index)
        for i in sorted(index_list_of_deletion, reverse=True):
            del homeworks_tuple_list_new[i]
        self.close_db()
        return homeworks_tuple_list_new

    ################not tested yet
    def get_homework_bool(self, students_session_tuple):
        self.open_db()
        homework_list_details = []
        for index, value in enumerate(students_session_tuple):
            if index == 1:
                self.mycursor.execute(f"select user_name from student_info where personal_id = '{value}';'")
                self.myresult = self.mycursor.fetchall()
                homeworks_tuple_list_all = self.get_homeworks_names(self.myresult[0])
                homeworks_tuple_list_new = copy.deepcopy(homeworks_tuple_list_all)
                homeworks_tuple_list_not_finished = self.check_if_homework_finished(homeworks_tuple_list_all, value)
                for homework_tuple in homeworks_tuple_list_new:
                    if homework_tuple in homeworks_tuple_list_not_finished:  # homework tuple consist of homework_name, homework_id and course_id
                        homework_list_details.append((homework_tuple, "Not finished"))
                    else:
                        homework_list_details.append((homework_tuple, "Finished"))
        self.close_db()
        return homework_list_details

    ############# not tested yet
    def check_if_homework_finished_before(self, homework_id, user_name):
        self.open_db()
        self.mycursor.execute(f"SELECT personal_id From student_info where user_name = '{user_name}';")
        self.myresult = self.mycursor.fetchall()
        personal_id_list = []
        for item in self.myresult:
            personal_id_list.append(str(item[0]))
        self.mycursor.execute(f"SELECT homework_stat_id From finished_homework_ab_es where personal_id = '{personal_id_list[0]}' and homework_id = '{homework_id}';")
        self.myresult = self.mycursor.fetchall()
        finished_list = []
        for item in self.myresult:
            finished_list.append(str(item[0]))
        self.close_db()
        if finished_list == []:
            return False
        else:
            return True

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

    # material tab methods

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

    def get_lecture(self, course_name_m_course, lecture_name):
        self.open_db()
        self.mycursor.execute(f"select course_id from course_ab_es where course_name = '{course_name_m_course}';")
        self.myresult = self.mycursor.fetchall()
        course_list = []
        for item in self.myresult:
            course_list.append(item[0])
        course_id = course_list[0]
        self.mycursor.execute(f"select id from pdf_files_mil where course_id = {course_id} and file_name = '{lecture_name}';")
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
