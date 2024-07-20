import os


class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET KEY')


class Development(Config):
    """Development configuration"""
    DEBUG = True


class Testing(Config):
    """Testing configuration"""
    TESTING = True


class Production(Config):
    """Production configuration"""
    DEBUG = False
