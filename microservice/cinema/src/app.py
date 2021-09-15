"""
Microservice en python pour la gestion de cinema.
Ce microservice permet:
- la récupération d"une liste de cinema
- l"ajout d"un nouveau cinema
- la recherche d"un cinema en fonction d"un nom de ville
"""
from flask import Flask, request
from os import environ
from pymongo import MongoClient
from bson.objectid import ObjectId
from uuid import uuid4

app = Flask("cinema")
client = MongoClient(
    host=environ.get("MONGODB_HOST", "localhost"),
    port=int(environ.get("MONGODB_PORT", 27017)))
database = client.cinema

utilisateurs_collection = database.utilisateurs

@app.route("/<id>", methods=["GET"])
def trouver_cinema_par_id(id):
    print(id)
    cinema = utilisateurs_collection.find_one({"_id": ObjectId(id)})
    cinema["_id"] = str(cinema["_id"])
    return cinema

@app.route("/", methods=["GET"])
def trouver_tous_cinemas():
    cinemas_cursor = utilisateurs_collection.find({})
    cinemas = []
    for cinema in cinemas_cursor:
        print(cinema)
        cinema["_id"] = str(cinema["_id"])
        cinemas.append(cinema)
    return {"results":cinemas}

@app.route("/", methods=["POST"])
def sauvegarder_nouveau_cinema():
    nouveau_cinema = request.json
    nouveau_cinema["_id"] = ObjectId()
    nouveau_id = utilisateurs_collection.insert_one(nouveau_cinema).inserted_id
    nouveau_cinema["_id"] = str(nouveau_id)
    return nouveau_cinema

app.run(port=int(environ.get("PORT", 80)))