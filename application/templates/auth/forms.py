from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Käyttäjä", [validators.Length(min=2)])
    password = PasswordField("Salasana", [validators.Length(min=10, max=30, message="Salasanan tulee olla vähintään 10 kirjainta ja eniintään 30")])
    email = StringField("Sähköposti", [validators.Length(min=2)])
    class Meta:
        csrf = False

class EditForm(FlaskForm):
    newusername = StringField("Laske kokoukselle hinta", [validators.Length(min=2)])
    newemail = StringField("sähköposti", [validators.Length(min=2)])

    class Meta:
        csrf = False

class ChangePassForm(FlaskForm):
    oldpass = PasswordField("Vanha salasana", [validators.Length(min=2)])
    newpass = PasswordField("Uusi salasana", [validators.Length(min=2, max=30, message="Salasanan tulee olla 10-30 kirjainta pitkä")])
    confirmpass = PasswordField("Hyväksy salasana", [validators.Length(min=2, max=30)])

    class Meta:
        csrf = False

