from unittest import TestCase

from database.Database import Database
from src.exceptions.Exceptions import NoteDeleted


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
        note = self.database.get_note_by_id(1)
        self.assertTrue(note.deleted)

    def test_cant_modify_deleted_note(self):
        # given
        title = "Title"
        content = "Content"
        self.database.create_note(title, content)
        # when
        self.database.delete_note_by_id(1)
        # then
        note = self.database.get_raw_note_by_id(1)
        self.assertIsNone(note)

    def tearDown(self):
        self.database.close_conn()
