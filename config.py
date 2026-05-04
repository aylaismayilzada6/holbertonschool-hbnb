import os

class Config:
    """Base configuration with default settings."""
    # Not an API key! This secures sessions and tokens.
    SECRET_KEY = os.getenv('SECRET_KEY', 'hc_dev_secret_key_12345')
    
    # Common settings
    JSON_SORT_KEYS = False
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Configuration for local development."""
    DEBUG = True
    # In a real app, you might have a local DB URI here
    ENV = 'development'

class TestingConfig(Config):
    """Configuration for running unit tests."""
    TESTING = True
    DEBUG = True
    # Use a separate secret key or DB for testing to avoid data loss
    SECRET_KEY = 'test_secret_key'

class ProductionConfig(Config):
    """Configuration for the live server."""
    # In production, DEBUG MUST be False
    DEBUG = False
    # Force the use of an environment variable for the secret key
    SECRET_KEY = os.getenv('SECRET_KEY') 

# Dictionary to easily switch between environments
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}