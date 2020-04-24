from flask import redirect, render_template, request, session, flash, url_for
from mask_site import app
#, db
from mask_site.forms import RegistrationForm
#from mask_site.models import order
from mask_site.emails import email_form
from flask_wtf.csrf import CSRFError


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        """
        ord = order(name=form.name.data, surname = form.surname.data, email=form.email.data, address= form.address.data, address_2= form.address_2.data, post_code= form.post_code.data,quantity= form.quantity.data )
        db.session.add(ord)
        db.session.commit()
        """
        email_form().send_emails()
        return redirect(url_for('confirm'))
    return render_template('formularz.html', title='Register', form=form)


@app.route("/potwierdzenie")
def confirm():
    return render_template('potwierdzenie.html')

"""
@app.route("/zamowienia")
def view():
    return render_template("zamowienia.html", values=order.query.all())

"""
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400
