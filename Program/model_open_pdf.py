import mysql.connector
from mysql.connector import Error
import os
import tempfile
import subprocess


class Open_pdf:
    def __init__(self):
        pass

    def open_lecture(self, lecture_record):
        try:
            if lecture_record:
                file_name, file_data = lecture_record

                # Write the binary data to a temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                    temp_file.write(file_data)
                    temp_path = temp_file.name

                # Open the temporary file using the default PDF viewer
                if os.name == "posix":
                    subprocess.call(["xdg-open", temp_path])
                elif os.name == "nt":
                    os.startfile(temp_path)
                else:
                    print("Unsupported operating system.")
            else:
                print("File not found.")

        except Error as e:
            print(f"Error: {e}")
