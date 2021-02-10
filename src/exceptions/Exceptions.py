class NoteNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)


class NoteDeleted(Exception):
    def __init__(self, message):
        super().__init__(message)


class WebException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(message)
