from application import db

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(30), nullable=False)
	lowink = db.Column(db.Boolean, nullable=False)

	def __init__(self, name):
		self.name = name
		self.lowink = False
