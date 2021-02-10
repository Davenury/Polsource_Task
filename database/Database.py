import sqlite3
from datetime import datetime

from database.Note import Note
from database.QueryExecutor import QueryExecutor
from definitions import DATABASE_FILE_NAME


class Database:
    def __init__(self, mode="Prod"):
        self.conn = self.create_connection(mode)
        self.query_executor = QueryExecutor(self.conn)
        self.query_executor.create_database()

    @staticmethod
    def create_connection(mode="Prod"):
        conn = None
        if mode == "Test":
            path = ":memory:"
        else:
            path = DATABASE_FILE_NAME
        try:
            conn = sqlite3.connect(path, check_same_thread=False)
        except sqlite3.Error as e:
            print(e)
        return conn

    def get_cursor(self):
        return self.conn.cursor()

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def create_note(self, title, content):
        created_date = datetime.now().timestamp()
        modified_date = created_date
        insert_tuple = (title, content, created_date, modified_date, 1, False)
        self.query_executor.create_note(insert_tuple)

    def get_note_by_id(self, id):
        note = self.query_executor.get_note_by_id(id)
        return Note(*note)

    def get_raw_note_by_id(self, id):
        return self.query_executor.get_note_by_id(id)

    def get_all_notes(self):
        notes = self.query_executor.get_all_notes()
        return [Note(*note) for note in notes]

    def update_note_by_id(self, note_id, title=None, content=None):
        self.query_executor.update_note(note_id, title, content)

    def delete_note_by_id(self, note_id):
        self.query_executor.delete_note(note_id)

    def holy_hand_granade(self):
        self.query_executor.holy_hand_granade()
