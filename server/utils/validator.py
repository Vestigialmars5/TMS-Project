import re

MIN_NAME = 2
MAX_NAME = 30
MIN_PASSWORD = 8

def clean_string(s):
    return s.strip()

def clean_email(email):
    return email.strip().lower()

def clean_name(name):
    return name.strip().title()

def is_valid_email(email):
    regex = r'[^@]+@[^@]+\.[^@]+'
    return re.match(regex, email)

def is_strong_password(password):
    return len(password) >= MIN_PASSWORD

def is_valid_name(name):
    return MIN_NAME <= len(name) <= MAX_NAME
