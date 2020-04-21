from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    name = StringField('Imię', validators=[DataRequired(),Length(min=2,max=20)])
    surname = StringField('Nazwisko', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    address = StringField('Ulica, numer mieszkania', validators=[DataRequired(),Length(min=2,max=20)])
    address_2 = StringField('Miejscowość', validators=[DataRequired()])
    post_code = StringField('Kod Pocztowy', validators=[DataRequired()])
    quantity = StringField('Ilość', validators=[DataRequired()])
    submit = SubmitField('Wyślij')