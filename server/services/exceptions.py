# Database exceptions
class DatabaseError(Exception):
    pass


class DatabaseQueryError(DatabaseError):
    status_code = 500
    def __init__(self, message="Database Query Error"):
        self.message = message
        super().__init__(self.message)
