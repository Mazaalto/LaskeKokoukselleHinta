from application import db
from application.models import Base

class User(Base):
# koska sana user on varattu avainsana myöh. käytettävässä PostgreSQLssä  niin käytetään
# tietokantataulussa nimeä account
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    tasks = db.relationship("Task", backref='account', lazy=True)

    def __init__(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
