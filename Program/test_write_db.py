"""Test the Write_db class in the model_write_db file."""
import mysql.connector

from unittest.mock import MagicMock
import unittest
from model_write_db import Write_db
from model_read_db import Read_db


class TestWriteDb(unittest.TestCase):
    def setUp(self):
        """Set up the test case."""
        self.write_db = Write_db()
        self.read_db = Read_db()

    def test_init(self):
        """Test the __init__ method."""
        self.assertIsInstance(self.write_db, Write_db)

    def test_open_db(self):
        """Test the open_db method."""
        self.write_db.open_db()
        self.assertIsInstance(
            self.write_db.mydb, mysql.connector.connection_cext.CMySQLConnection
        )

    def test_close_db(self):
        """Test the close_db method."""
        mock_cursor = MagicMock()
        mock_db = MagicMock()
        mock_db.cursor.return_value = mock_cursor
        write_db = Write_db()
        write_db.mydb = mock_db
        write_db.mycursor = mock_cursor

        write_db.close_db()

        mock_cursor.close.assert_called_once()
        mock_db.close.assert_called_once()

# gui_register test methods
    def test_insert_student_info(self):
        write_db = Write_db()
        first_name = "test"
        last_name = "test"
        email = "test@test.test"
        password = "test"
        username = "test"
        personal_id = "9999999999"
        year_of_study = 1
        name_of_program = "Medicine"
        write_db.insert_student_info(first_name, last_name, email, username, password, personal_id, year_of_study, name_of_program)
        write_db.open_db()
        write_db.mycursor.execute(f"SELECT * FROM student_info WHERE personal_id = '{personal_id}' And first_name = '{first_name}' And last_name = '{last_name}' And user_name = '{username}' And email = '{email}' And year_of_study = '{year_of_study}' And program_name = '{name_of_program}';")
        myresult = write_db.mycursor.fetchall()
        myresult_expected = [("9999999999", "test", "test", "test", "test", "test@test.test", "Medicine", 1)]
        self.assertEqual(myresult, myresult_expected)
        write_db.mycursor.execute(f"Select * From student_course_ab_es Where personal_id = '{personal_id}';")
        myresult2 = write_db.mycursor.fetchall()
        myresult2_expected = [('9999999999', 6), ('9999999999', 7), ('9999999999', 8), ('9999999999', 9), ('9999999999', 10)]
        self.assertEqual(myresult2, myresult2_expected)
        write_db.mycursor.execute(f"DELETE FROM student_course_ab_es WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        self.assertEqual(myresult, myresult_expected)
        write_db.mycursor.execute(f"DELETE FROM student_info WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.close_db()

# gui_main_window test methods
    # material_tab
    def test_add_new_note_to_db(self):
        self.first_name = "a"
        self.last_name = "a"
        self.email = "a@a.a"
        self.password = "a"
        self.username = "a"
        self.personal_id = "1234567890"
        self.year_of_study = "1"
        self.name_of_program = "Programing"
        self.write_db.insert_student_info(self.first_name, self.last_name, self.email, self.username, self.password, self.personal_id, self.year_of_study, self.name_of_program)
        note_name = "note1"
        note_data = "note1_data"
        self.write_db.add_new_note_to_db(note_name, note_data, "a")
        expected_note_data = 'note1_data'
        self.assertEqual(self.read_db.get_note_data("note1", "a"), expected_note_data)
        self.write_db.open_db()
        self.write_db.mycursor.execute("DELETE FROM notes_mil WHERE note_name = 'note1';")
        self.write_db.mydb.commit()
        self.write_db.close_db()
        self.write_db.open_db()
        self.write_db.mycursor.execute(f"DELETE FROM student_course_ab_es WHERE personal_id = '{self.personal_id}';")
        self.write_db.mydb.commit()
        self.write_db.mycursor.execute(f"DELETE FROM student_info WHERE personal_id = '{self.personal_id}';")
        self.write_db.mydb.commit()
        self.write_db.close_db()
    # def tearDown(self):
    #     self.db = None

    # team_session tab
    def test_store_session(self):
        self.create_user()
        session_name = "session1"
        self.write_db.store_session(session_name, self.username)
        self.assertEqual(self.read_db.check_session_name(session_name,self.username), True)
        self.write_db.open_db()
        self.write_db.mycursor.execute(f"DELETE FROM session_ab_es WHERE session_name = '{session_name}';")
        self.write_db.mydb.commit()
        self.write_db.close_db()
        self.delete_user()

    def test_store_students_in_session(self):
        self.create_user()
        student_session_list = [("a a", "1234567890")]
        session_name = "session1"
        expected_session_name_list = ["session1"]
        self.write_db.store_session(session_name, self.username)
        session_id = self.read_db.get_session_id(session_name, self.username)
        self.write_db.store_students_in_session(student_session_list, session_id)
        self.assertEqual(self.read_db.get_sessions_names(self.username), expected_session_name_list)
        self.write_db.open_db()
        self.write_db.mycursor.execute(f"DELETE FROM student_session_ab_es WHERE session_id = '{session_id[0]}';")
        self.write_db.mycursor.execute(f"DELETE FROM session_ab_es WHERE session_name = '{session_name}';")
        self.write_db.mydb.commit()
        self.write_db.close_db()
        self.delete_user()

    def create_user(self):
        self.first_name = "a"
        self.last_name = "a"
        self.email = "a@a.a"
        self.password = "a"
        self.username = "a"
        self.personal_id = "1234567890"
        self.year_of_study = "1"
        self.name_of_program = "Programing"
        self.write_db.insert_student_info(self.first_name, self.last_name, self.email, self.username, self.password, self.personal_id, self.year_of_study, self.name_of_program)

    def delete_user(self):
        self.write_db.open_db()
        self.write_db.mycursor.execute(f"DELETE FROM student_course_ab_es WHERE personal_id = '{self.personal_id}';")
        self.write_db.mydb.commit()
        self.write_db.mycursor.execute(f"DELETE FROM student_info WHERE personal_id = '{self.personal_id}';")
        self.write_db.mydb.commit()
        self.write_db.close_db()


if __name__ == "__main__":
    unittest.main()
