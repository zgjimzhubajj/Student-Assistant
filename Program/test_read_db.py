"""Test the Read_db class in the model_read_db module."""
import mysql.connector

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
    # This test imports Read_db from the your_module module and creates an
    # instance of it by calling its __init__ method.
    # The test then checks whether the created object is an instance of the
    # Read_db class.

    def test_init(self):
        """Test the __init__ method."""
        self.assertIsInstance(self.read_db, Read_db)

    # 3---------------------------------------------------------------------------------------------
    # this test checks whether the open_db() method of the Read_db class
    # successfully connects to a MySQL database by asserting that the mydb
    # attribute of the Read_db object is an
    # instance of mysql.connector.connection_cext.CMySQLConnection.
    # This ensures that the open_db() method has opened
    # a valid database connection.

    def test_open_db(self):
        """Test the open_db method."""
        self.read_db.open_db()
        self.assertIsInstance(
            self.read_db.mydb, mysql.connector.connection_cext.CMySQLConnection
        )

    # 4---------------------------------------------------------------------------------------------
    # This test uses the unittest module and the MagicMock class
    # to create a mock database connection and cursor object,
    # which are assigned to the mydb and mycursor attributes
    # of the Read_db object.
    # The close_db() function is then called, and the assert_called_once()
    # method is used to verify that the close() method was called once on both
    # the cursor and the database connection.
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
    # This test case creates an instance of the Read_db class,
    # calls the get_programs_names method, and checks that the return value
    # is a list of strings.
    # The isinstance function is used to check that programs is a list,
    # and the all function is used to check that all items
    # in the list are strings.

    def test_get_programs_names(self):
        """Test the get_programs_names method."""
        db = Read_db()
        programs = db.get_programs_names()
        assert isinstance(programs, list)
        assert all(isinstance(program, str) for program in programs)

    # 6---------------------------------------------------------------------------------------------
    # Initializes a Read_db object
    # Ensures that the username 'testuser' does not already exist in the
    # database by calling the check_user_name_exists method with the username
    # 'testuser' as an argument
    # Adds a new user with the username 'testuser' to the database
    # Ensures that the username 'testuser' now exists in the database
    # by calling the check_user_name_exists method with the username 'testuser'
    # as an argument
    # Removes the user with the username 'testuser' from the database

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

        # Remove any existing users with the personal ID '1234567892'
        read_db.open_db()
        read_db.mycursor.execute(
            "DELETE FROM student_info WHERE personal_id = '6565656565';"
        )
        read_db.mydb.commit()
        read_db.close_db()

        # # Ensure that the personal ID '1234567892' does not already exist in
        # # the database
        # assert read_db.check_personal_id_exists("6565656565") == False

        # Add a new user with the personal ID '1234567892'
        read_db.open_db()
        read_db.mycursor.execute(
            "INSERT INTO student_info (first_name, last_name, user_name, email, password, personal_id, year_of_study, program_name) VALUES ('Test', 'User', 'testuser', 'testuser@test.com', 'testpassword', '6565656565', '1', 'Medicine');"
        )
        read_db.mydb.commit()
        read_db.close_db()

        # # Ensure that the personal ID '1234567892' now exists in the database
        # assert read_db.check_personal_id_exists("6565656565") == True

        # Remove the user with the personal ID '1234567892'
        read_db.open_db()
        read_db.mycursor.execute(
            "DELETE FROM student_info WHERE personal_id = '6565656565';"
        )
        read_db.mydb.commit()
        read_db.close_db()

# gui_forgot_password methods
    # 8------------------------------------------------------------------------------------------------
    # This code snippet is a Python function for testing password
    # retrieval functionality in a database.
    # The function starts by creating a database object
    # using the Read_db() class.
    # The function then calls the retrieve_password() method on the
    # database object to retrieve a password associated with a specific user.
    # The retrieve_password() method takes several parameters,
    # including first name, last name, email, username, phone number,
    # department, and returns the associated password.
    # The function then asserts that the retrieved password is equal to
    # the expected password, "mypassword123".
    # This test function can be used to verify that the password retrieval
    # functionality of the database is working correctly.

    def test_retrieve_password(self):
        pass

# gui_login methods
    # 9------------------------------------------------------------------------------------------------
    #  the purpose of the "test_check_login_stats" method is to verify that the
    # "check_login_stats" method of the Read_db class is working correctly and
    # returning the expected results for different input combinations.
    def test_check_login_stats(self):
        pass


if __name__ == "__main__":
    unittest.main()
