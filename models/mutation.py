from graphene import (
    ObjectType,
    Mutation,
    Int,
    String,
    Field,
)
from api_config import (
    db,
)

from .objects import (
    Club,
    Entrenador,
    Jugador
)

from .club import Club as ClubModel
from .entrenador import Entrenador as EntrenadorModel
from .jugador import Jugador as JugadorModel

#------------Mutations clubes---------------#

class createClub(Mutation):
    class Arguments:
        name = String(required=True)
        telefono = String(required=True)
        direccion_sede = String(required=True)
        entrenador_fk = Int(required=True)  # Atributo de relacion a entrenador
    
    club = Field(lambda: Club)

    def mutate(self, info, name, telefono, direccion_sede, entrenador_fk):
        club = ClubModel(name=name, telefono=telefono, direccion_sede=direccion_sede, entrenador_fk=entrenador_fk)

        db.session.add(club)
        db.session.commit()

        return createClub(club=club)

class updateClub(Mutation):
    class Arguments:
        club_id = Int(required=True)
        name = String()
        telefono = String()
        direccion_sede = String()
        entrenador_fk = Int()

    club = Field(lambda: Club)

    def mutate(self, info, club_id, name=None, telefono=None, direccion_sede=None, entrenador_fk=None):
        club = ClubModel.query.get(club_id)
        if club:
            if name:
                club.name = name
            if telefono:
                club.telefono = telefono
            if direccion_sede:
                club.direccion_sede = direccion_sede
            if entrenador_fk:
                club.entrenador_fk = entrenador_fk

            db.session.add(club)
            db.session.commit()

        return updateClub(club=club)


class deleteClub(Mutation):
    class Arguments:
        club_id = Int(required=True)

    club = Field(lambda: Club)

    def mutate(self, info, club_id):
        club = ClubModel.query.get(club_id)
        if club:
            db.session.delete(club)
            db.session.commit()

        return deleteClub(club=club)
    

#------------Mutations entrenadores---------------#

class createEntrenador(Mutation):
    class Arguments:
        name = String(required=True)
        last_name = String(required=True)

    entrenador = Field(lambda: Entrenador)

    def mutate(self, info, name, last_name):
        entrenador = EntrenadorModel(name=name, last_name=last_name)

        db.session.add(entrenador)
        db.session.commit()

        return createEntrenador(entrenador=entrenador)


class updateEntrenador(Mutation):
    class Arguments:
        entrenador_id = Int(required=True)
        name = String()
        last_name = String()

    entrenador = Field(lambda: Entrenador)

    def mutate(self, info, entrenador_id, name=None, last_name=None):
        entrenador = EntrenadorModel.query.get(entrenador_id)
        if entrenador:
            if name:
                entrenador.name = name
            if last_name:
                entrenador.last_name = last_name

            db.session.add(entrenador)
            db.session.commit()

        return updateEntrenador(entrenador=entrenador)
    
    
class deleteEntrenador(Mutation):
    class Arguments:
        entrenador_id = Int(required=True)

    entrenador = Field(lambda: Entrenador)

    def mutate(self, info, entrenador_id):
        entrenador = EntrenadorModel.query.get(entrenador_id)
        if entrenador:
            db.session.delete(entrenador)
            db.session.commit()

        return deleteEntrenador(entrenador=entrenador)
    

#------------Mutations jugadores---------------#

class createJugador(Mutation):
    class Arguments:
        name = String(required=True)
        last_name = String(required=True)
        club_fk = Int(required=True)  # Atributo de relacion a entrenador
    
    jugador = Field(lambda: Jugador)

    def mutate(self, info, name, last_name, club_fk):
        jugador = JugadorModel(name=name, last_name=last_name, club_fk=club_fk)

        db.session.add(jugador)
        db.session.commit()

        return createJugador(jugador=jugador)

class updateJugador(Mutation):
    class Arguments:
        jugador_id = Int(required=True)
        name = String()
        last_name = String()
        club_fk = Int()

    jugador = Field(lambda: Jugador)

    def mutate(self, info, jugador_id, name=None, last_name=None, club_fk=None):
        jugador = JugadorModel.query.get(jugador_id)
        if jugador:
            if name:
                jugador.name = name
            if last_name:
                jugador.last_name = last_name
            if club_fk:
                jugador.club_fk = club_fk

            db.session.add(jugador)
            db.session.commit()

        return updateJugador(jugador=jugador)

class deletejugador(Mutation):
    class Arguments:
        jugador_id = Int(required=True)

    jugador = Field(lambda: Jugador)

    def mutate(self, info, jugador_id):
        jugador = JugadorModel.query.get(jugador_id)
        if jugador:
            db.session.delete(jugador)
            db.session.commit()

        return deletejugador(jugador=jugador)


class Mutation(ObjectType):
    createClub = createClub.Field()
    updateClub = updateClub.Field()
    deleteClub = deleteClub.Field()

    createEntrenador = createEntrenador.Field()
    updateEntrenador = updateEntrenador.Field()
    deleteEntrenador = deleteEntrenador.Field()

    createJugador = createJugador.Field()
    updateJugador = updateJugador.Field()
    deletejugador = deletejugador.Field()