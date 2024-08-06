# Auth exceptions
class AuthError(Exception):
    def __init__(self, message="Authentication Error"):
        self.message = message
        super().__init__(self.message)

class InvalidCredentials(AuthError):
    def __init__(self, message="Invalid Credentials"):
        self.message = message
        super().__init__(self.message)

class Unauthorized(AuthError):
    def __init__(self, message="Unauthorized"):
        self.message = message
        super().__init__(self.message)


# Database exceptions
class DatabaseError(Exception):
    def __init__(self, message="Database Error"):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionError(DatabaseError):
    def __init__(self, message="Database Connection Error"):
        self.message = message
        super().__init__(self.message)

class DatabaseQueryError(DatabaseError):
    def __init__(self, message="Database Query Error"):
        self.message = message
        super().__init__(self.message)


# JWT exceptions
class JWTError(Exception):
    def __init__(self, message="JWT Error"):
        self.message = message
        super().__init__(self.message)
    

class InvalidToken(JWTError):
    def __init__(self, message="Invalid Token"):
        self.message = message
        super().__init__(self.message)

class ExpiredToken(JWTError):
    def __init__(self, message="Expired Token"):
        self.message = message
        super().__init__(self.message)

class RevokedToken(JWTError):
    def __init__(self, message="Revoked Token"):
        self.message = message
        super().__init__(self.message)

class TokenBlacklistedError(JWTError):
    def __init__(self, message="Token Blacklisted"):
        self.message = message
        super().__init__(self.message)

