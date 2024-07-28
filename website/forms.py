from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class LoginForm(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired()], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'User Name'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Password'})
    submit = SubmitField('Login', render_kw={'class': 'btn btn-outline-secondary', 'id': 'button-addon2'})


class SignUpForm(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired()], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'User Name'})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Too Short'), EqualTo('rePassword', 'Passwords must match!')], render_kw={'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Password'})
    rePassword = PasswordField('Repeat Password', validators=[DataRequired()], render_kw={'class': 'form-control', 'id': 'floatingRePassword', 'placeholder': 'Repeat Password'})
    submit = SubmitField('Sign up!', render_kw={'class': 'btn btn-outline-secondary', 'id': 'button-addon2'})