class NoteNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)


class NoteDeleted(Exception):
    def __init__(self, message):
        super().__init__(message)
