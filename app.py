from flask import Flask, redirect, render_template, request, session, flash, url_for
from forms import RegistrationForm
app = Flask(__name__)

orders=[{
    'name': 'Ellon',
    'address': 'Sydney'
}]

app.config['SECRET_KEY'] = 'b0c363e1be51668250911243a6b1c167'


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", orders=orders)

@app.route("/register", methods=["GET","POST"])
def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            return redirect(url_for('confirm'))
        return render_template('formularz.html',title='Register',form=form)

@app.route("/potwierdzenie")
def confirm():
    return render_template('potwierdzenie.html',orders=orders)
    


    
    
    


if __name__ == "__main__":
    app.run(debug=True)


      
    