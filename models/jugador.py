from api_config import db


class Jugador(db.Model):
    __tablename__ = "jugador"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    club_fk = db.Column(db.Integer, db.ForeignKey("club.id"))
    club = db.relationship('Club', backref='jugador_club')