from api_config import db


class Entrenador(db.Model):
    __tablename__ = "entrenador"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
"""     fk_club = db.Column(db.Integer, db.ForeignKey("club.id"))
    club = db.relationship("Club") """
