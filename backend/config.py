class Settings:
    DATABASE_URL = 'your_database_url_here'
    API_CONFIG = {
        'API_KEY': 'your_api_key_here',
        'API_SECRET': 'your_api_secret_here'
    }
    FILE_UPLOAD_SETTINGS = {
        'MAX_UPLOAD_SIZE': 10 * 1024 * 1024,  # 10 MB
        'ALLOWED_EXTENSIONS': {'pdf', 'docx', 'png', 'jpg'}
    }