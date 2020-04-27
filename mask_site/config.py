import os


class Config:
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RC_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY =os.environ.get('RC_PRIVATE_KEY')
    RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}
    WTF_CSRF_SECRET_KEY = os.environ.get('CSRF_KEY)
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #db = SQLAlchemy(app)
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')