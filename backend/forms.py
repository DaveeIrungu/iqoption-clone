from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SignUpform(FlaskForm):
    firstname = StringField('First name', validators=[DataRequired()])
    lastname = StringField('Last name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    password  = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('I accept the Terms & Conditions and confirm that I am 18 years old or older.',
                               validators=[DataRequired()])
    submit = SubmitField('OPEN AN ACCOUNT FOR FREE')

class Loginform(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('LOGIN')