from time import sleep
from unittest import TestCase

from database.Database import Database


class VersionedNoteTest(TestCase):
    def setUp(self):
        self.database = Database("Test")

    def test_versioned_note(self):
        # given
        title = "Title"
        content = "Content"
        self.database.create_note(title, content)
        # when
        sleep(1)
        self.database.update_note_by_id(1, "Title2", "Modified")
        # then
        notes = self.database.get_versioned_note_by_id(1)
        self.assertEqual(notes[0].title, title)
        self.assertEqual(notes[1].title, "Title2")

    def test_count_number_of_versions(self):
        # given
        title = "Title"
        content = "Content"
        self.database.create_note(title, content)
        # when
        sleep(1)
        self.database.update_note_by_id(1, "Title2", "Modified")
        # then
        result = self.database.query_executor.execute("Select count(*) from Note_version")
        self.assertEqual(result[0], 2)

    def tearDown(self):
        self.database.close_connection()
