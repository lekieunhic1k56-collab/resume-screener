# Application Configuration

class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///app.db'
    SECRET_KEY = 'your_secret_key_here'

class ProductionConfig(Config):
    DATABASE_URI = 'postgres://user:password@localhost/prod_db'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///dev.db'

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'sqlite:///test.db'