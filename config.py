from decouple import config

# Setup database path
DATABASE_URI = config("DATABASE_URL")
if DATABASE_URI.startswith("postgres://"):
    DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)

# Default Flask app configuration 
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config('SECRET_KEY', default='guess-me')
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Production environment configuration
class ProductionConfig(Config):
    DEBUG = False

# Staging environment configuration
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

# Development environment configuration
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

# Testing development configuration
class TestingConfig(Config):
    TESTING = True