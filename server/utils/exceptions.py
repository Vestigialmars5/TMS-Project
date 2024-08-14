# Database exceptions
class DatabaseError(Exception):
    pass


class DatabaseQueryError(DatabaseError):
    status_code = 500
    def __init__(self, message="Database Query Error"):
        self.message = message
        super().__init__(self.message)


class ValidationError(Exception):
    pass


class DataValidationError(ValidationError):
    status_code = 400
    def __init__(self, message="Invalid Data"):
        self.message = message
        super().__init__(self.message)