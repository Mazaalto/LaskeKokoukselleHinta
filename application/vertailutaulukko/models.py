from application import db

class Vertailu(db.Model):

    __tablename__ = "vertailu"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
#tarkoituksena on lisätä vertailutauluun tietoja, miten kalliiksi kokous tulee.
#esim auton hintainen yms.
    name = db.Column(db.String(144), nullable=False)
    hinta = db.Column(db.Integer, nullable=False)

    def __init__(self, name, hinta):
        self.name = name
        self.hinta = hinta

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
