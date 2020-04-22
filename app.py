from flask import Flask, redirect, render_template, request, session, flash, url_for
from forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm

app = Flask(__name__)



app.config['SECRET_KEY'] = 'b0c363e1be51668250911243a6b1c167'


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", )

@app.route("/register", methods=["GET","POST"])
def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            print(f'We are sending masks for {form.name.data}')
            return redirect(url_for('confirm'))
        return render_template('formularz.html',title='Register',form=form)

@app.route("/potwierdzenie")
def confirm():
    return render_template('potwierdzenie.html')
    


    
    
    


if __name__ == "__main__":
    app.run(debug=True)


      
    