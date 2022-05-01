import os

from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    
    database_user=os.getenv('DATABASE_USERNAME')
    database_password=os.getenv('DATABASE_PASSWORD')
    database_url=os.getenv('DATABASE_POSTGRESS_URL')
    database_port=os.getenv('DATABASE_PORT')
    database_schema=os.getenv('DATABASE_SCHEMA')
    database_application_name = os.getenv('DATABASE_APPLICATION_NAME')
    
    DATABASE_USERNAME=os.getenv('DATABASE_USERNAME')
    DATABASE_PASSWORD=os.getenv('DATABASE_PASSWORD')
    DATABASE_URL=os.getenv('DATABASE_URL')
    DATABASE_PORT=os.getenv('DATABASE_PORT')
    DATABASE_SCHEMA = os.getenv('DATABASE_SCHEMA')
    DATABASE_APPLICATION_NAME = os.getenv('DATABASE_APPLICATION_NAME')
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}?application_name={}'.format(database_user,database_password,database_url,database_port,database_schema,database_application_name)
    JSON_SORT_KEYS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    
    AWS_REGION=os.getenv('AWS_REGION')
    AWS_ACCESS_ID=os.getenv('AWS_ACCESS_ID')
    AWS_SECRET_KEY=os.getenv('AWS_SECRET_KEY')
    AWS_BUCKET_NAME=os.getenv('AWS_BUCKET_NAME')
    AWS_BUCKET_FOLDER = os.getenv('AWS_BUCKET_FOLDER')
    SES_EMAIL_SOURCE = os.getenv('SES_EMAIL_SOURCE')
    SES_EMAIL_SOURCE = os.getenv('SES_EMAIL_SOURCE')
    SES_AWS_REGION_NAME= os.getenv('SES_AWS_REGION_NAME')


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ="postgresql://myuser:mypass@localhost:5432/farm_test"

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = dict(
    development = DevelopmentConfig,
    testing = TestingConfig,
    staging = StagingConfig,
    production = ProductionConfig
)
    