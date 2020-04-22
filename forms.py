from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    name = StringField('Imię', validators=[DataRequired(),Length(min=2,max=20)])
    surname = StringField('Nazwisko', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(),Email(),Length(min=2,max=120)])
    address = StringField('Ulica, numer mieszkania', validators=[DataRequired(),Length(min=2,max=120)])
    address_2 = StringField('Miejscowość', validators=[DataRequired(),Length(min=2,max=120)])
    post_code = StringField('Kod Pocztowy', validators=[DataRequired(),Length(min=2,max=20)])
    quantity = StringField('Ilość', validators=[DataRequired(),Length(min=1,max=2)])
    submit = SubmitField('Wyślij')