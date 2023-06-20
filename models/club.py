from api_config import db


class Club(db.Model):
    __tablename__ = "club"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    telefono = db.Column(db.String(16))
    direccion_sede = db.Column(db.String(50))
    entrenador_fk = db.Column(db.Integer, db.ForeignKey("entrenador.id"))
    entrenador = db.relationship('Entrenador', backref='club_entrenador')