from application import db

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(30), nullable=False)
	type = db.Column(db.Integer, nullable=False)
	lowink = db.Column(db.Boolean, nullable=False)

	account_id = db.Column(db.Integer, db.ForeignKey('account.id'),  nullable=False)

	def __init__(self, name, type):
		self.name = name
		self.type = type
		self.lowink = False
