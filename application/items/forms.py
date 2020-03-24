from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class ItemForm(FlaskForm):
	name = StringField("Item name", [validators.Length(min=4)])
	type = StringField("Item type")
	lowink = BooleanField("Ink low")

	class Meta:
		csrf = False
