from time import sleep
from unittest import TestCase

from database.Database import Database


class UpdateNoteTest(TestCase):
    def setUp(self):
        self.database = Database("Test")

    def test_update_note(self):
        # given
        title = "Title"
        content = "Content"
        self.database.create_note(title, content)
        # when
        sleep(1)
        self.database.update_note_by_id(1, "Title2", "Modified")
        # then
        result = self.database.get_raw_note_by_id(1)
        self.assertEqual("Title2", result[0])
        self.assertEqual("Modified", result[1])
        self.assertNotEqual(result[2], result[3])

    def test_update_one_note(self):
        # given
        title = "Title"
        content = "Content"
        title2 = "Title2"
        content2 = "Content2"
        self.database.create_note(title, content)
        self.database.create_note(title2, content2)
        # when
        sleep(1)
        self.database.update_note_by_id(1, "Title2", "Modified")
        # then
        result = self.database.get_raw_note_by_id(1)
        unchanged_note = self.database.get_note_by_id(2)
        self.assertEqual("Title2", result[0])
        self.assertEqual("Modified", result[1])
        self.assertNotEqual(result[2], result[3])
        self.assertTrue(unchanged_note.title_and_content_equals(title2, content2))

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
        self.database.close_conn()
