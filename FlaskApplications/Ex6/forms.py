from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email
from flask_wtf import FlaskForm


class SigupForm(FlaskForm):
    fullName = StringField('Full Name', validators=[InputRequired()])
    email = StringField('E-Mail', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[InputRequired()])
    submit = SubmitField('Login')
