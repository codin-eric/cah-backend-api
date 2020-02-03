"""
Todo
 - Crear sala
    - La sala debe morir despues de no recibir request por n tiempo
    - La sala da un hash de sala con el que cada usuario se suma
    - El juego comienza cuando todos los jugadores dan su ok
"""

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from utils import Sala

app = Flask(__name__)
api = Api(app)

salas = {}


def abort_si_sala_no_existe(sala_hash):
    salas_hashes = [sala.hash for sala in salas]
    if sala_hash not in salas_hashes:
        abort(404, message=f"Sala {sala_hash} no existe")


parser = reqparse.RequestParser()
parser.add_argument("task")


class ListaSalas(Resource):
    def post(self):
        sala = Sala()
        salas[sala.hash] = sala
        return {"sala_hash": sala.hash}, 201

    def get(self):
        lst = list(salas.keys())
        return {"sala_hash": lst}, 201


##
## Setup the Api resource routing here
##
api.add_resource(ListaSalas, "/crear_sala")


if __name__ == "__main__":
    app.run(debug=True)
