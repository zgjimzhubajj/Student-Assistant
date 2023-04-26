"""Test the Write_db class in the model_write_db file."""
import mysql.connector

from unittest.mock import MagicMock
import unittest
from model_write_db import Write_db


class TestWriteDb(unittest.TestCase):
    def setUp(self):
        """Set up the test case."""
        self.write_db = Write_db()
        self.db = Write_db()

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

# gui_register methods
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
        print(myresult)
        myresult_expected = [("9999999999", "test", "test", "test", "test", "test@test.test", "Medicine", 1)]
        self.assertEqual(myresult, myresult_expected)
        write_db.mycursor.execute(f"DELETE FROM student_info WHERE personal_id = '{personal_id}';")
        write_db.mydb.commit()
        write_db.close_db()

    # def tearDown(self):
    #     self.db = None


if __name__ == "__main__":
    unittest.main()
