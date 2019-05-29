import os


class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BUILD_NUMBER = "##BUILD_NUMBER##"
    BUILD_ID = "##BUILD_ID##"
    BUILD_TAG = "##BUILD_TAG##"
    GIT_COMMIT = "##GIT_COMMIT##"


class LocalConfig(BaseConfig):
    """Development configuration"""
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://loki:d0nt4get@localhost:5432/loki')


class TestingConfig(BaseConfig):
    """Test environment configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL', 'sqlite:///test.db')


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://loki:d0nt4get@localhost:5432/loki')


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
