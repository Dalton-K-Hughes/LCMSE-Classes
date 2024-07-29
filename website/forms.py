from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length

class LoginForm(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired()], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'User Name'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Password'})
    submit = SubmitField('Login', render_kw={'class': 'btn btn-outline-secondary', 'id': 'button-addon2'})


class SignUpForm(FlaskForm):
    classChoices = [
        ('Section 1-8', 'Period 2: Intro to Software Technology'),
        ('Section 2-8', 'Period 3: Foundations of Investing'),
        ('Section 3-8', 'Period 3: Foundations of Investing'),
        ('Section 4-8', 'Period 3: Foundations of Interactive Design'),
        ('Section 5-8', 'Period 3: Foundations of Interactive Design'),
        ('Section 1-6: FBA', 'Period 4: Foundations of Business Administration'), 
        ('Section 2-6: FBA', 'Period 5: Foundations of Business Administration'),
        ('Section 3-6: FBA', 'Period 4: Foundations of Business Administration'),
        ('Section 4-6: FBA', 'Period 5: Foundations of Business Administration'),
        ('Section 1-7: FID', 'Period 6: Foundations of Interactive Design'),
        ('Section 2-7: FID', 'Period 7: Foundations of Interactive Design'),
        ('Section 3-7: FID', 'Period 6: Foundations of Interactive Design'),
        ('Section 4-7: FID', 'Period 7: Foundations of Interactive Design'),
]
    
    user_name = StringField('User Name', validators=[DataRequired()], render_kw={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'User Name'})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Too Short'), EqualTo('rePassword', 'Passwords must match!')], render_kw={'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Password'})
    rePassword = PasswordField('Repeat Password', validators=[DataRequired()], render_kw={'class': 'form-control', 'id': 'floatingRePassword', 'placeholder': 'Repeat Password'})
    classChoice = SelectField('Class', validators=[DataRequired()], choices=classChoices, render_kw={'class': 'form-control'})
    adminPassword = PasswordField('Admin Password', render_kw={'class': 'form-control', 'id': 'floatingAdminPassword', 'placeholder': 'Admin Password'})
    submit = SubmitField('Sign up!', render_kw={'class': 'btn btn-outline-secondary', 'id': 'button-addon2'})
    
class AssignmentSubmission(FlaskForm):
    pass