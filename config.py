import os

class Config:
    # General settings
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'e832a2c5e4188a228bdd938d4b574677d8bc4faed67d3de3')  # Default in case FLASK_SECRET_KEY is not set

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://tony:whpu4CqOykeHuw2sdeQUrETBkHfCp24u@dpg-csdhupd6l47c73dbe57g-a/schedule_db_zdhr')

    # Other settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    FLASK_APP = os.getenv('FLASK_APP', 'app.py')
