from unittest import TestCase

from database.Database import Database


class CreateNoteTest(TestCase):
    def setUp(self):
        self.database = Database("Test")

    def test_create_note_and_check_quantity(self):
        # given
        title = "Title"
        content = "Content"
        # when
        self.database.create_note(title, content)
        result = self.database.query_executor.execute('Select count(*) from Notes')
        # then
        self.assertEqual(1, result[0])

    def test_create_note_and_check_content(self):
        # given
        title = "Title"
        content = "content"
        version = 1
        deleted = False
        # when
        self.database.create_note(title, content)
        result = self.database.query_executor.execute('Select * from Notes')
        # then
        self.assertEqual(title, result[0])
        self.assertEqual(content, result[1])
        self.assertEqual(version, result[4])
        self.assertEqual(deleted, result[5])

    def test_create_note_and_check_in_note_version(self):
        # given
        title = "Title"
        content = "content"
        # when
        self.database.create_note(title, content)
        result = self.database.query_executor.execute('Select * from Note_version')
        # then
        self.assertEqual(title, result[1])
        self.assertEqual(content, result[2])

    def tearDown(self):
        self.database.close_connection()
