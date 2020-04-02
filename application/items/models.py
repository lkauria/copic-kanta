from application import db

from sqlalchemy.sql import text

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(30), nullable=False)
	colorcode = db.Column(db.String(30), nullable=False)
	ptype = db.Column(db.String(30), nullable=False)
#        type_id = db.Column(db.Integer, ForeignKey('type.id') nullable=False)
#        ptype = relationship("Type", uselist=False)

	lowink = db.Column(db.Boolean, nullable=False)

	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

	def __init__(self, name, colorcode, ptype):
                self.name = name
                self.ptype = ptype
                self.lowink = False
                self.colorcode = colorcode


	def get_id(self):
	        return self.id

	def get_lowink(self):
		return self.lowink


	@staticmethod
	def find_lowink():
		stmt = text("SELECT Item.colorcode, Item.name, Item.type"
				" FROM Item WHERE Item.lowink = 1"
				" GROUP BY Item.account_id")
		result = db.engine.execute(stmt)

		response = []
		for row in result:
                    response.append({"colorcode":row[0], "name":row[1], "type":row[2]})

		return response
