"""Test the Write_db class in the model_write_db file."""
import mysql.connector

from unittest.mock import MagicMock, Mock
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
        pass

    # def tearDown(self):
    #     self.db = None


if __name__ == "__main__":
    unittest.main()
