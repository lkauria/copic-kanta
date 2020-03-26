from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SelectField

class ItemForm(FlaskForm):
	name = StringField("Item name", [validators.Length(min=3)])
	colorcode = StringField("Item colorcode", [validators.Length(min=3)])
	type = SelectField(u'Item type', choices=[('1', 'Sketch'), ('2','Ciao'), ('3', 'Ink Bottle')])
	lowink = BooleanField("Ink low")

	class Meta:
		csrf = False
