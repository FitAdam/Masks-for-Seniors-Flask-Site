from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    name = StringField('Imię', validators=[DataRequired(),Length(min=2,max=20)])
    surname = StringField('Nazwisko', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(),Email(),Length(min=2,max=120)])
    address = StringField('Ulica, numer mieszkania', validators=[DataRequired(),Length(min=2,max=120)])
    address_2 = StringField('Miejscowość', validators=[DataRequired(),Length(min=2,max=120)])
    post_code = StringField('Kod Pocztowy', validators=[DataRequired(),Length(min=2,max=20)])
    quantity = SelectField('Ilość',[DataRequired()],
                        choices=[('1', '1'),
                                 ('2', '2'),
                                 ('3', '3'),
                                 ('4', '4'),
                                 ('5', '5'),
                                 ('6', '6')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Wyślij')

#
 #   def validate_email(self, email):
  #      duplicate = dublicate.query.filter_by(email=email.data).first()
   #     if user:
    #        raise ValidationError('That email is taken. Please choose a different one.')