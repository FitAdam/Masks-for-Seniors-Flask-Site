from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
import os


app = Flask(__name__)

csrf = CSRFProtect(app)
csrf.init_app(app)
app.config['WTF_CSRF_SECRET_KEY'] = os.environ.get('RC_PRIVATE_KEY')
app.config['SECRET_KEY'] = os.environ.get('RC_PRIVATE_KEY')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']= os.environ.get('RC_PUBLIC_KEY')
app.config['RECAPTCHA_PRIVATE_KEY']=os.environ.get('RC_PRIVATE_KEY')
app.config['RECAPTCHA_DATA_ATTRS'] = {'theme': 'dark'}
#db = SQLAlchemy(app)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)



from mask_site import routes
