from unittest import TestCase

from database.Database import Database
from src.exceptions.Exceptions import NoteNotFound


class GetAllNotesTest(TestCase):
    def setUp(self):
        self.database = Database("Test")

    def test_get_all_notes(self):
        # given
        title1 = "Title"
        content1 = "Content"
        title2 = "Title2"
        content2 = "Content2"
        self.database.create_note(title1, content1)
        self.database.create_note(title2, content2)
        # when
        result = self.database.get_all_notes()
        # then
        self.assertTrue(len(result) == 2)
        self.assertTrue(result[0].title_and_content_equals(title1, content1))
        self.assertTrue(result[1].title_and_content_equals(title2, content2))

    def test_with_empty_database(self):
        # given

        # when then
        with self.assertRaises(NoteNotFound):
            self.database.get_all_notes()

    def tearDown(self):
        self.database.close_connection()
