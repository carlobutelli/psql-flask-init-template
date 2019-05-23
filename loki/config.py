import os


class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = dict(
        title='Loki Identity Verification Service',
        uiversion=1,
        description="API for identity verification with MiTek",
        specs_route="/swagger"
    )


class LocalConfig(BaseConfig):
    """Development configuration"""
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(BaseConfig):
    """Test environment configuration"""
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://hades:d0nt4get@localhost:5432/idv')
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
