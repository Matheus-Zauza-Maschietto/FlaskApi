from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo
from flask_wtf import FlaskForm


class SigupForm(FlaskForm):
    full_name = StringField('Full Name', validators=[InputRequired()])
    email = StringField('E-Mail', validators=[InputRequired(), Email(message="Insert valid email format")])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Signup')
    

class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[InputRequired(), Email(message="Insert valid email format")])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')