from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b0c363e1be51668250911243a6b1c167'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']='6LdX8uwUAAAAAC4R350hvMBHaRymxShSRNNrxfMo'
app.config['RECAPTCHA_PRIVATE_KEY']='6LdX8uwUAAAAAH3Bg1IpiTVIEh1IvHz2ZGwvMbTp'
app.config['RECAPTCHA_OPTIONS']= {'theme':'black'}
db = SQLAlchemy(app)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from mask_site import routes
