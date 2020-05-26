from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class TaskForm(FlaskForm):
    name = StringField("Kokouksen nimi", [validators.Length(min=3)])
    done = BooleanField("Kokous pidetty")
  
    class Meta:
        csrf = False
