from application import db

class Colorcode(db.Model):

	__tablename__ = "colorcode"

	id = db.Column(db.Integer, primary_key=True)

	code = db.Column(db.String(30), nullable=False, unique=True)

	def __init__(self, code):
		self.code = code

	@staticmethod
	def colorcode_list():
		return Colorcode.query.order_by(Colorcode.code)
