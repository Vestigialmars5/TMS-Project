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
    SQLALCHEMY_DATABASE_URI = os.getenv('TMS_DATABASE_URL')
    SQLALCHEMY_BINDS = {
        'wms': os.getenv('WMS_DATABASE_URL')
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    """Development configuration"""
    DEBUG = True


class Testing(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_BINDS = {
        "wms": "sqlite:///:memory:"
    }


class Production(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
