from pymongo import MongoClient
from bson.objectid import ObjectId
from os import environ

MONGO_HOST = environ.get("MONGO_HOST", "localhost")
MONGO_PORT = int(environ.get("MONGO_PORT", 27017))

client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
voyage_bdd = client.voyage
voyages_collection = voyage_bdd.voyages

def trouver_tout_voyages():
    voyages = []
    for voyage in voyages_collection.find():
        voyage["_id"] = str(voyage["_id"])
        voyages.append(voyage)
    return voyages

def trouver_voyage_par_id(id):
    voyage = voyages_collection.find_one({"_id":ObjectId(id)})
    voyage["_id"] = str(voyage["_id"])
    return voyage

def sauvegarder_voyage(voyage):
    voyage["_id"] = ObjectId()
    voyages_collection.insert_one(voyage)
    voyage["_id"] = str(voyage["_id"])
    return voyage

if __name__ == '__main__':
    voyage = {
        "titre":"M2i road trip",
        "description":"Un super trip sous le soleil du nord de la france, Road trip dans le manifique metro lillois",
        "villes":["Villeneuve d'ascq", "Lille", "Armentieres"]
    }
    sauvegarder_voyage(voyage)
    trouver_tout_voyages()

    