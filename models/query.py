from graphene import (
    ObjectType,
    Field,
    String,
    Boolean,
    List,
    Int
)

from .club import Club as ClubModel
from .entrenador import Entrenador as EntrenadorModel
from .jugador import Jugador as JugadorModel
from .objects import Club, Entrenador, Jugador

class Query(ObjectType):
    clubes = List(lambda: Club, name=String(), id=Int(), telefono=String(), direccion_sede=String())
    entrenadores = List(lambda: Entrenador)
    jugadores = List(lambda: Jugador)

    def resolve_clubes(self, info, id=None, order_by_name=None):
        query = Club.get_query(info=info)
        if id:
            query = query.filter(ClubModel.id==id)
        if order_by_name:
            query = query.order_by(ClubModel.name)
        return query.all()
    
    def resolve_entrenadores(self, info):
        query = Entrenador.get_query(info=info)
        return query.all()
    
    def resolve_entrenador(self, info, id):
        entrenador = EntrenadorModel.query.get(id)
        return entrenador

    def resolve_jugadores(self, info):
        query = Jugador.get_query(info=info)
        return query.all()  

    def resolve_jugador(self, info, id):
        jugador = JugadorModel.query.get(id)
        return jugador