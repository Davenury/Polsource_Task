import sqlite3
from datetime import datetime

from database.sql_scripts import create_note_table, create_note_version_table
from src.exceptions.Exceptions import NoteDeleted, NoteNotFound


def check_note(note_id, note):
    if note is None:
        raise NoteNotFound(f"Note with {note_id} wasn't found.")
    if note[5] is True:
        raise NoteDeleted("Note was deleted and can't be modified.")


class QueryExecutor:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def create_database(self):
        try:
            self.cursor.execute(create_note_table)
            self.cursor.execute(create_note_version_table)
        except sqlite3.Error as e:
            print(e)

    def create_note(self, insert_tuple):
        self.create_in_note_table(insert_tuple)
        self.create_in_version_table(self.cursor.lastrowid, insert_tuple)

    def create_in_note_table(self, insert_tuple):
        create_note_sql = 'Insert into notes VALUES (?,?,?,?,?,?)'
        self.cursor.execute(create_note_sql, insert_tuple)
        self.connection.commit()

    def create_in_version_table(self, note_id, insert_tuple):
        create_note_version_sql = 'Insert into note_version VALUES (?,?,?,?,?,?,?)'
        self.cursor.execute(create_note_version_sql, (note_id, *insert_tuple))
        self.connection.commit()

    def execute(self, command):
        self.cursor.execute(command)
        return self.cursor.fetchone()

    def get_note_by_id(self, id):
        query = 'Select *, ROWID from Notes where ROWID=?'
        self.cursor.execute(query, (id,))
        note = self.cursor.fetchone()
        if note is None:
            raise NoteNotFound(f"Note by id: {id} wasn't found")
        return note

    def get_all_notes(self):
        query = 'Select *, ROWID from Notes'
        self.cursor.execute(query)
        notes = self.cursor.fetchall()
        if not notes:
            raise NoteNotFound("There aren't any notes in database")
        return notes

    def update_note(self, note_id, title, content):
        note = self.get_note_by_id(note_id)
        check_note(note_id, note)
        if note[5] == 0:
            deleted = False
        else:
            deleted = True
        now = datetime.now().timestamp()
        if title is None:
            title = note[0]
        if content is None:
            content = note[1]
        self.create_in_version_table(note_id, (title, content, note[2], now, note[4]+1, deleted))
        update_query = 'UPDATE Notes set title=?, content=?, modified=?, version=? where ROWID = ?'
        self.cursor.execute(update_query, (title, content, now, note[4]+1, note_id))
        self.connection.commit()

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        check_note(note_id, note)
        now = datetime.now().timestamp()
        self.create_in_version_table(note_id, (note[0], note[1], note[2], now, note[4]+1, True))
        update_query = 'Delete from Notes where ROWID = ?'
        self.cursor.execute(update_query, (note_id, ))
        self.connection.commit()

    def holy_hand_granade(self):
        self.cursor.execute('DROP TABLE Note_version')
        self.cursor.execute('DROP TABLE Notes')
