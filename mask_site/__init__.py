from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b0c363e1be51668250911243a6b1c167'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']='6LdX8uwUAAAAAC4R350hvMBHaRymxShSRNNrxfMo'
app.config['RECAPTCHA_PRIVATE_KEY']='6LdX8uwUAAAAAH3Bg1IpiTVIEh1IvHz2ZGwvMbTp'
app.config['RECAPTCHA_OPTIONS']= {'theme':'black'}
db = SQLAlchemy(app)

from mask_site import routes
