class Validator:
    MIN_NAME = 2
    MAX_NAME = 30
    MIN_PASSWORD = 8

    @staticmethod
    def is_valid_email(email):
        # TODO: implementation here
        pass

    @staticmethod
    def is_valid_username(username):
        # TODO: implementation here
        pass

    @staticmethod
    def is_valid_password(password):
        # TODO: implementation here
        pass

    @staticmethod
    def is_valid_role(role):
        # TODO: implementation here, return role id
        pass

    @staticmethod
    def is_one_word(string):
        # TODO: implementation here
        pass

    @staticmethod
    def has_numbers_or_specials(string):
        # TODO: implementation here
        pass

    @staticmethod
    def is_valid_length(string):
        return Validator.MIN_NAME <= len(string) <= Validator.MAX_NAME
