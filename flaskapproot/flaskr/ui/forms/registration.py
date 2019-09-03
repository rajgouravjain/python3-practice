from flask_wtf import FlaskForm
from wtforms import (StringField,IntegerField,
                    TextField,PasswordField, BooleanField, SubmitField,RadioField)
from wtforms.validators import DataRequired, Email, EqualTo
from models.owners import Owner
from models.pets import Pet

class OwnerRegistrationForm(FlaskForm):
    name = StringField(label="Name",validators=[DataRequired()])
    password = PasswordField(label="Password",validators=[DataRequired(),EqualTo(fieldname='password_confirm',message="Password must match")])
    password_confirm = PasswordField(label="Password Confirm",validators=[DataRequired()])
    email = StringField(label='Email',validators=[DataRequired(),Email()])
    submit = SubmitField(label="Register now!")
    def check_email(self, field):
        # Check if not None for that user email!
        if Owner.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self, field):
        # Check if not None for that username!
        if Owner.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')

class PetRegistrationForm(FlaskForm):
    name = StringField(label="Name",validators=[DataRequired()])
    breed = StringField(label="Breed",validators=[DataRequired()])
    submit = SubmitField(label="Register now!")
