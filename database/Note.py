from datetime import datetime


class Note:
    def __init__(self, *args):
        self.title = args[0]
        self.content = args[1]
        self.created = args[2]
        self.modified = args[3]
        self.version = args[4]
        self.deleted = args[5]

    def get_created_date(self):
        return self.prepare_date(self.created)

    def get_modified_date(self):
        return self.prepare_date(self.modified)

    @staticmethod
    def prepare_date(timestamp):
        return datetime.fromtimestamp(timestamp)

    def title_and_content_equals(self, title, content):
        return self.title == title and self.content == content
