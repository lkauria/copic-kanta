from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.type.models import Type
from application.colorcode.models import Colorcode

class ItemForm(FlaskForm):
	name = StringField("Item name", [validators.Length(min=3)])
	colorcode = StringField("Item colorcode", [validators.Length(min=3)])
	type = QuerySelectField(u'Item type', query_factory = Type.type_list, get_label='name')

	class Meta:
		csrf = False


class PersonalItemForm(FlaskForm):
	name = StringField("Item name", [validators.Length(min=3)])
	colorcode = QuerySelectField(u'Item colorcode', query_factory = Colorcode.colorcode_list, get_label='code')
	type = QuerySelectField(u'Item type', query_factory = Type.type_list, get_label='name')

	class Meta:
		csrf = False


