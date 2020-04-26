from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from mask_site.config import Config


csrf = CSRFProtect()
mail = Mail()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    csrf.init_app(app)
    mail.init_app(app)
    from mask_site.main.routes import main
    from mask_site.emails_package.routes import customers
    from mask_site.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(customers)
    app.register_blueprint(errors)

    return app
