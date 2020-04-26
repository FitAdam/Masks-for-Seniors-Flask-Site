from flask import Blueprint, redirect, render_template, request, session, flash, url_for
from flask_wtf.csrf import CSRFError
from mask_site.emails_package.forms import RegistrationForm
from mask_site.emails_package.emails import email_form


customers = Blueprint('customers', __name__)



@customers.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        """
        ord = order(name=form.name.data, surname = form.surname.data, email=form.email.data, address= form.address.data, address_2= form.address_2.data, post_code= form.post_code.data,quantity= form.quantity.data )
        db.session.add(ord)
        db.session.commit()
        """
        email_form().send_emails()
        return redirect(url_for('main.confirm'))
    return render_template('formularz.html', title='Register', form=form)

@customers.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400

