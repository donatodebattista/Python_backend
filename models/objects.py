from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
)
from graphene import (
    Int,
    String
)
from models.club import Club as ClubModel
from models.entrenador import Entrenador as EntrenadorModel
from models.jugador import Jugador as JugadorModel


class Club(SQLAlchemyObjectType):
    class Meta:
        model = ClubModel
    name = String(description='representa el nombre de la persona')

class Entrenador(SQLAlchemyObjectType):
    class Meta:
        model = EntrenadorModel
        # exclude_fields = ('fk_persona')

class Jugador(SQLAlchemyObjectType):
    class Meta:
        model = JugadorModel