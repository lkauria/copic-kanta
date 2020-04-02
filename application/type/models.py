
from application import db

class Type(db.Model):

    __tablename__ = "type"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(30), unique=True, nullable=False)


    def __init__(self, name):
        self.name = name

    @staticmethod
    def type_list():
        return Type.query

