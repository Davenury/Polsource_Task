from unittest import TestCase

from database.Database import Database
from src.exceptions.Exceptions import NoteDeleted, NoteNotFound


class DeleteNoteTest(TestCase):
    def setUp(self):
        self.database = Database("Test")

    def test_delete_note(self):
        # given
        title = "Title"
        content = "Content"
        self.database.create_note(title, content)
        # when
        self.database.delete_note_by_id(1)
        # then
        with self.assertRaises(NoteNotFound):
            note = self.database.get_note_by_id(1)

    def test_cant_modify_deleted_note(self):
        # given
        title = "Title"
        content = "Content"
        self.database.create_note(title, content)
        # when
        self.database.delete_note_by_id(1)
        # then
        with self.assertRaises(NoteNotFound):
            note = self.database.get_raw_note_by_id(1)

    def tearDown(self):
        self.database.close_connection()
