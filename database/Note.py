from datetime import datetime


class Note:
    def __init__(self, *args, offset=0):
        self.title = args[0+offset]
        self.content = args[1+offset]
        self.created = args[2+offset]
        self.modified = args[3+offset]
        self.version = args[4+offset]
        self.deleted = args[5+offset]
        self.id = args[6] if offset == 0 else args[0]

    def get_created_date(self):
        return self.prepare_date(self.created)

    def get_modified_date(self):
        return self.prepare_date(self.modified)

    @staticmethod
    def prepare_date(timestamp):
        return datetime.fromtimestamp(timestamp)

    def title_and_content_equals(self, title, content):
        return self.title == title and self.content == content

    def get_json(self):
        return self.__dict__
