from flask import Blueprint, redirect, render_template, request, session, flash, url_for

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")


@main.route("/potwierdzenie")
def confirm():
    return render_template('potwierdzenie.html')



"""
@app.route("/zamowienia")
def view():
    return render_template("zamowienia.html", values=order.query.all())

"""
