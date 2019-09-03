from flask_wtf import FlaskForm
from wtforms import (IntegerField, StringField, BooleanField,
                    PasswordField,  SubmitField)
from wtforms.validators import Email, EqualTo, DataRequired

from wtforms.validators import ValidationError

class OwnerLoginForm(FlaskForm):
    email  = StringField(label="Email",validators=[DataRequired(),Email()])
    password = PasswordField(label="Password",validators=[DataRequired()])
    submit = SubmitField(label="Log In")
    
