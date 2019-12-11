from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

from models import User


class RegistrationForm(FlaskForm):
    name = StringField('Accountname',
                           validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "2 characters to 20 characters."})
   
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "2 characters to 20 characters."})
    api_code = StringField('Api Code', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "2 characters to 20 characters."})
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, name):   #check 資料庫是否已有該username
        user = User.query.filter_by(name=name.data).first()
        if user:    #can find
            raise ValidationError('That username is taken. Please choose a different one.')  #會在該欄位下面跑出訊息


class LoginForm(FlaskForm):
    name = StringField('Account',
                        validators=[DataRequired(), Length(min=2, max=20
                            , message='Account at least 2 characters maximum 20 characters ')], render_kw={"placeholder": "Account"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ResetPasswordForm(FlaskForm):
    original_password = PasswordField('Current Password', validators=[DataRequired(), Length(min=6, max=20, message='Password at least 6 characters maximum 20 characters')],
                             render_kw={"placeholder": "Please input current password."})
    password = PasswordField('New Password', validators=[DataRequired(), Length(min=6, max=20, message='Password at least 6 characters maximum 20 characters')],
                             render_kw={"placeholder": "Please input new password."})
    confirm_password = PasswordField('New Password Confirm', validators=[DataRequired(), EqualTo('password', message='Password is not the same.')],
                                     render_kw={"placeholder": "Please try again."})
    submit = SubmitField('Confirm')