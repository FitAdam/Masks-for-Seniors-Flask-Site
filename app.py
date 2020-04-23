from flask import Flask, redirect, render_template, request, session, flash, url_for
from forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b0c363e1be51668250911243a6b1c167'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']='6LdX8uwUAAAAAC4R350hvMBHaRymxShSRNNrxfMo'
app.config['RECAPTCHA_PRIVATE_KEY']='6LdX8uwUAAAAAH3Bg1IpiTVIEh1IvHz2ZGwvMbTp'
app.config['RECAPTCHA_OPTIONS']= {'theme':'black'}
db = SQLAlchemy(app)


class order(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name,email):
        self.name = name
        self.email = email

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", )

@app.route("/register", methods=["GET","POST"])
def register():
        form = RegistrationForm()
        if form.validate_on_submit():


            nm = form.name.data
            ord = order(name=form.name.data,email=form.email.data)
            db.session.add(ord)
            db.session.commit()
            print(f'We are sending masks for ',nm)
            return redirect(url_for('confirm'))
        return render_template('formularz.html',title='Register',form=form)


@app.route("/potwierdzenie")
def confirm():
    return render_template('potwierdzenie.html')
    

@app.route("/zamowienia")
def view():
    return render_template("zamowienia.html", values=order.query.all())
    
    
    


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


      
    