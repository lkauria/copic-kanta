from application import db
from sqlalchemy import text

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(144), unique=True, nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    items = db.relationship("Item", backref='account', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.admin = False

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_admin(self):
        return False

    @staticmethod
    def most_items():
        stmt = text("SELECT Account.username, COUNT(Item.id) AS item FROM Account" " LEFT JOIN Item ON Account.id = Item.account_id" " GROUP BY Account.username" " ORDER BY item DESC")
        result = db.engine.execute(stmt)
        response = []
        for row in result:
            response.append({"username:":row[0], "id":row[1]})
       
        return response
