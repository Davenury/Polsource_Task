from unittest import TestCase

from database.Database import Database
from src.exceptions.Exceptions import NoteNotFound


class GetNoteByIdTest(TestCase):
    def setUp(self):
        self.database = Database("Test")

    def test_get_note_by_id(self):
        # given
        self.database.create_note("Title", "Content")
        # when
        note = self.database.get_note_by_id(1)
        # then
        self.assertEqual(note.title, "Title")
        self.assertEqual(note.content, "Content")

    def test_no_note_like_this(self):
        # given

        # when then
        with self.assertRaises(NoteNotFound):
            self.database.get_note_by_id(2)

    def tearDown(self):
        self.database.close_connection()
