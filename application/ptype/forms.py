
from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PtypeForm(FlaskForm):
    name = StringField("Product type name", [validators.Length(min=3)])

    class Meta:
        csrf = False
