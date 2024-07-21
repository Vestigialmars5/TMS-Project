import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES'))
    DATABASE_URL = os.getenv('DATABASE_URL')
    WMS_DATABASE_URL = os.getenv('WMS_DATABASE_URL')


class Development(Config):
    """Development configuration"""
    DEBUG = True


class Testing(Config):
    """Testing configuration"""
    TESTING = True


class Production(Config):
    """Production configuration"""
    DEBUG = False
