import os
from decouple import config

class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SECRET = "very sensitive text"
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/aqua'

class DevelopmentConfig(Config):
    FLASK_APP = "run.py"
    Development = True
    SECRET = "very sensitive text"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/aqua'

class TestingConfig(Config):
    Testing = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://kisakye:kisakye6@localhost/aquaculture_test'
    DEBUG = True

class StagingConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'staging' : StagingConfig,
    'production' : ProductionConfig
}