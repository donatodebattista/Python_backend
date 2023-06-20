import psycopg2
# import contextlib

db_params = dict(
    host="localhost",
    database="postgres",
    port=5432,
    user="postgres",
    password="password"
)

def conect_to_db(db_params):
    print("Connecting to PostgreSQL database...")
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    cur.close()
    conn.close()


def get_db(db_params):
    print("Connecting to PostgreSQL database...")
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    return cur, conn

def get_all_clubes():
    connection, con = get_db(db_params)
    connection.execute("select * from club")
    respuesta = []    
    for club in connection.fetchall():
        datos = {}
        datos['id'] = club[0]
        datos['nombre'] = club[1]
        datos['telefono'] = club[2]
        datos['direccion_sede'] = club[3]
        #datos['email'] = club[4]
        respuesta.append(datos)
    
    return respuesta

def get_by_id(id):
    connection, con = get_db(db_params)
    connection.execute(f"select * from club where id = {id}")
    club = connection.fetchone()
    datos = {}
    datos['id'] = club[0]
    datos['nombre'] = club[1]
    datos['telefono'] = club[2]
    datos['direccion_sede'] = club[3]
    #datos['email'] = club[4]
    
    return datos

""" 
def get_club_entrenador(id):
    connection, con = get_db(db_params)
    connection.execute(f"select * from entrenador e join club c on (e.fk_club = c.id) where c.id ={id}")
    clubes = connection.fetchall()
    datos_clubes = {}
    if len(clubes) > 0:
        datos_clubes['id'] = clubes[0][3]
        datos_clubes['nombre'] = clubes[0][4]
        datos_clubes['apellido'] = clubes[0][5]
        #datos_clubes['email'] = clubes[0][6]
        datos_clubes['deptos'] = []
        clubes = []
        for club in clubes:
            datos_club = {}
            datos_club['id'] = club[0]
            datos_club['nombre'] = club[1]
            datos_club['deptos'].append(datos_club)
    
    return datos_clubes
    
def delete_by_id(id):
    connection, con = get_db(db_params)
    connection.execute(f"delete from club where id = {id}")
    con.commit()

def insert_club(name, telfono, direccion_sede, email):
    print("tratando de insertar persona")
    connection, con = get_db(db_params)
    connection.execute(f"insert into club (name, telefono, direccion_sede, email) values ('{name}', '{telfono}', '{direccion_sede}', '{email}') returning id")
    club = connection.fetchone()
    con.commit()
    return club[0]

def update_club_email(id, email):
    connection, con = get_db(db_params)
    connection.execute(f"update club set email = '{email}' where id = {id}")
    con.commit()



def get_club_jugador(id):
    connection, con = get_db(db_params)
    connection.execute(f"select * from jugador j join club c on (j.fk_club = c.id) where c.id ={id}")
    jugadores = connection.fetchall()
    datos_jugadores = {}
    if len(jugadores) > 0:
        datos_jugadores['id'] = jugadores[0][3]
        datos_jugadores['nombre'] = jugadores[0][4]
        datos_jugadores['apellido'] = jugadores[0][5]
        jugadores = []
        for jugador in jugadores:
            datos_jugador = {}
            datos_jugador['id'] = jugador[0]
            datos_jugador['nombre'] = jugador[1]
            datos_jugador['deptos'].append(datos_jugador) """