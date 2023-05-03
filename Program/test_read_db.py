"""Test the Read_db class in the model_read_db module."""
import mysql.connector
import sqlite3
from unittest.mock import MagicMock
import unittest
from model_read_db import Read_db
from model_write_db import Write_db


class TestReadDb(unittest.TestCase):
    """Test the Read_db class in the model_read_db module."""

    # 1---------------------------------------------------------------------------------------------
    def setUp(self):
        """Set up the test case."""
        self.read_db = Read_db()

    # 2---------------------------------------------------------------------------------------------
    def test_init(self):
        """Test the __init__ method."""
        self.assertIsInstance(self.read_db, Read_db)

    # 3---------------------------------------------------------------------------------------------

    def test_open_db(self):
        """Test the open_db method."""
        self.read_db.open_db()
        self.assertIsInstance(
            self.read_db.mydb, mysql.connector.connection_cext.CMySQLConnection
        )

    # 4---------------------------------------------------------------------------------------------
    def test_close_db(self):
        """Test the close_db method."""
        mock_cursor = MagicMock()
        mock_db = MagicMock()
        mock_db.cursor.return_value = mock_cursor
        read_db = Read_db()
        read_db.mydb = mock_db
        read_db.mycursor = mock_cursor

        read_db.close_db()

        mock_cursor.close.assert_called_once()
        mock_db.close.assert_called_once()

# gui_register methods
    # 5---------------------------------------------------------------------------------------------

    def test_get_programs_names(self):
        """Test the get_programs_names method."""
        db = Read_db()
        programs = db.get_programs_names()
        assert isinstance(programs, list)
        assert all(isinstance(program, str) for program in programs)

    # 6---------------------------------------------------------------------------------------------

    def test_check_user_name_exists(self):
        """Test the check_user_name_exists method."""
        # Initialize Read_db object
        read_db = Read_db()

        # Remove any existing users with the username 'testuser'
        read_db.open_db()
        read_db.mycursor.execute(
            "DELETE FROM student_info WHERE user_name = 'testuser';"
        )
        read_db.mydb.commit()
        read_db.close_db()

        # Ensure that the username 'testuser' does not already exist in
        # the database
        assert read_db.check_user_name_exists("testuser") == False

        # Add a new user with the username 'testuser'
        read_db.open_db()
        read_db.mycursor.execute(
            "INSERT INTO student_info (first_name, last_name, user_name, email, password, personal_id, year_of_study, program_name) VALUES ('Test', 'User', 'testuser', 'testuser@test.com', 'testpassword', '123456789', '1', 'Medicine');"
        )
        read_db.mydb.commit()
        read_db.close_db()

        # Ensure that the username 'testuser' now exists in the database
        assert read_db.check_user_name_exists("testuser") == True

        # Remove the user with the username 'testuser'
        read_db.open_db()
        read_db.mycursor.execute(
            "DELETE FROM student_info WHERE user_name = 'testuser';"
        )
        read_db.mydb.commit()
        read_db.close_db()

    # 7---------------------------------------------------------------------------------------------
    def test_check_personal_id_exists(self):
        """Test the check_personal_id_exists method."""
        # Initialize Read_db object
        read_db = Read_db()

        # Remove any existing users with the personal ID '6565656565'
        read_db.open_db()
        read_db.mycursor.execute(
            "DELETE FROM student_info WHERE personal_id = '6565656565';"
        )
        read_db.mydb.commit()
        read_db.close_db()

        # # Ensure that the personal ID '6565656565' does not already exist in
        # # the database
        assert read_db.check_personal_id_exists("6565656565") == False

        # Add a new user with the personal ID '6565656565'
        read_db.open_db()
        read_db.mycursor.execute(
            "INSERT INTO student_info (first_name, last_name, user_name, email, password, personal_id, year_of_study, program_name) VALUES ('Test', 'User', 'testuser', 'testuser@test.com', 'testpassword', '6565656565', '1', 'Medicine');"
        )
        read_db.mydb.commit()
        read_db.close_db()

        # # Ensure that the personal ID '6565656565' now exists in the database
        assert read_db.check_personal_id_exists("6565656565") == True

        # Remove the user with the personal ID '6565656565'
        read_db.open_db()
        read_db.mycursor.execute(
            "DELETE FROM student_info WHERE personal_id = '6565656565';"
        )
        read_db.mydb.commit()
        read_db.close_db()

# gui_forgot_password methods
    # 8------------------------------------------------------------------------------------------------

    def test_retrieve_password(self):
        read_db = Read_db()
        write_db = Write_db()
        first_name = "test"
        last_name = "test"
        email = "test@test.test"
        password = "test"
        username = "test"
        personal_id = "9999999999"
        year_of_study = "1"
        name_of_program = "Medicine"
        write_db.insert_student_info(first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program)
        self.assertEqual(read_db.retrieve_password(first_name, last_name, email, username, personal_id, year_of_study, name_of_program), password)
        write_db.open_db()
        write_db.mycursor.execute(f"DELETE FROM student_course_ab_es WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.mycursor.execute(f"DELETE FROM student_info WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.close_db()

    def test_check_user_exists(self):
        read_db = Read_db()
        write_db = Write_db()
        first_name = "test"
        last_name = "test"
        email = "test@test.test"
        username = "test"
        name_of_program = "Medicine"
        personal_id = "9999999999"
        year_of_study = "1"
        password = "test"
        write_db.insert_student_info(first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program)
        self.assertEqual(read_db.check_user_exists(first_name, last_name, email, username, name_of_program, personal_id, year_of_study), True)
        read_db.open_db()
        read_db.mycursor.execute(f"select * from student_course_ab_es where personal_id = '{personal_id}';")
        myresult = read_db.mycursor.fetchall()
        expected_result = True
        if myresult == []:
            expected_result = False
        self.assertEqual(expected_result, True)
        write_db.open_db()
        write_db.mycursor.execute(f"DELETE FROM student_course_ab_es WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.mycursor.execute(f"DELETE FROM student_info WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.close_db()
        read_db.close_db()



# # gui_login methods
#     # 9------------------------------------------------------------------------------------------------

    def test_check_login_stats(self):
        read_db = Read_db()
        write_db = Write_db()
        first_name = "test"
        last_name = "test"
        email = "test@test.test"
        password = "test"
        username = "test"
        personal_id = "9999999999"
        year_of_study = "1"
        name_of_program = "Medicine"
        write_db.insert_student_info(first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program)
        self.assertEqual(read_db.check_login_stats(username, password), True)
        write_db.open_db()
        write_db.mycursor.execute(f"DELETE FROM student_course_ab_es WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.mycursor.execute(f"DELETE FROM student_info WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.close_db()

#gui_main_window methods
    # team session tab
    def test_get_homework_detail(self):
        read_db = Read_db()
        write_db = Write_db()
        first_name = "test"
        last_name = "test"
        email = "test@test.test"
        password = "test"
        username = "test"
        personal_id = "9999999999"
        year_of_study = "1"
        name_of_program = "Medicine"
        write_db.insert_student_info(first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program)
        expected_list = [['homework6', '2023', '5', '20']]
        self.assertEqual(read_db.get_homework_detail("anatomy"), expected_list)
        write_db.open_db()
        write_db.mycursor.execute(f"DELETE FROM student_course_ab_es WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.mycursor.execute(f"DELETE FROM student_info WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.close_db()

    def test_get_course(self):
        read_db = Read_db()
        read_db = Read_db()
        write_db = Write_db()
        first_name = "test"
        last_name = "test"
        email = "test@test.test"
        password = "test"
        username = "test"
        personal_id = "9999999999"
        year_of_study = "1"
        name_of_program = "Medicine"
        write_db.insert_student_info(first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program)
        expected_list = ['anatomy']
        self.assertEqual(read_db.get_course(username), expected_list)
        write_db.open_db()
        write_db.mycursor.execute(f"DELETE FROM student_course_ab_es WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.mycursor.execute(f"DELETE FROM student_info WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.close_db()

    # Time management tab
    def test_get_first_name(self):
        first_name = "a"
        last_name = "a"
        email = "a@a.a"
        password = "a"
        username = "a"
        personal_id = "1234567890"
        year_of_study = "1"
        name_of_program = "Programing"
        read_db = Read_db()
        write_db = Write_db()
        read_db.open_db()
        write_db.insert_student_info(first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program)
        expected_first_name = "a"
        self.assertEqual(read_db.get_first_name(username), expected_first_name)
        write_db.open_db()
        write_db.mycursor.execute(f"DELETE FROM student_course_ab_es WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.mycursor.execute(f"DELETE FROM student_info WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.close_db()

    def test_get_homeworks(self):
        first_name = "a"
        last_name = "a"
        email = "a@a.a"
        password = "a"
        username = "a"
        personal_id = "1234567890"
        year_of_study = "1"
        name_of_program = "Programing"
        read_db = Read_db()
        write_db = Write_db()
        read_db.open_db()
        write_db.insert_student_info(first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program)
        expected_list = ['java homework1 2023-5-15', 'python homework2 2023-5-16', 'agile homework3 2023-5-17']
        self.assertEqual(read_db.get_homeworks(username), expected_list)
        write_db.open_db()
        write_db.mycursor.execute(f"DELETE FROM student_course_ab_es WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.mycursor.execute(f"DELETE FROM student_info WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.close_db()


if __name__ == "__main__":
    unittest.main()
