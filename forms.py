from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired, equal_to, length



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), length(min=3, max=20)])
    email = StringField('Email',
                        validators=[DataRequired()])
    planet = StringField('Favourite planet',
                         validators=[DataRequired()])
    #avatar = FileField(validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         length(min=6, message=('Please, enter stronger password')),
                                         equal_to('confirm_password')])
    confirm_password = PasswordField('Confirm password',
                                     validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Your email', validators=[DataRequired()])
    password = PasswordField('Your password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')
