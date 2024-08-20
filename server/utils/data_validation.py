import re
from server.utils.exceptions import DataValidationError

MIN_NAME = 2
MAX_NAME = 30
MIN_PASSWORD = 8

def clean_email(email):
    if not email or not isinstance(email, str):
        raise DataValidationError("Email Missing or Invalid")

    # Email contains @ and .
    regex = r'[^@]+@[^@]+\.[^@]+'
    email = email.strip().lower()
    
    if not re.match(regex, email):
        raise DataValidationError("Invalid Email")
    
    return email

def clean_name(name):
    if not name or not isinstance(name, str):
        raise DataValidationError("Invalid Name")

    name = name.strip().title()
    if not MIN_NAME <= len(name) <= MAX_NAME:
        raise DataValidationError("Invalid Name")
    
    # Check if name contains only alphabets
    if not name.isalpha():
        raise DataValidationError("Invalid Name")

    return name

def is_password_valid(password):
    if not password or not isinstance(password, str):
        return False
    return len(password) >= MIN_PASSWORD

def clean_phone_number(phone_number):
    if not phone_number or not isinstance(phone_number, str):
        raise DataValidationError("Phone Number Missing or Invalid")
    # Remove all non-digits except '+'
    phone_number = re.sub(r'[^\d+]', '', phone_number)

    if not len(phone_number) == 10:
        if not phone_number.startswith('+') or not len(phone_number) == 12:
            raise DataValidationError("Invalid Phone Number Length")
        else:
            return phone_number
    else:
        return phone_number

def clean_address(address):
    # TODO: Implement address validation service
    if not address or not isinstance(address, str):
        raise DataValidationError("Invalid Address")
    
    address = address.strip()
    
    if 0 >= len(address) < 10:
        raise DataValidationError("Invalid Address")
    
    return address

def clean_role_id(role_id):
    if not role_id or not isinstance(role_id, int):
        raise DataValidationError("Role ID Missing or Invalid")
    
    # Role ID must be between 1 and 7
    if not 0 < role_id <= 7:
        raise DataValidationError("Invalid Role ID")

    return role_id

