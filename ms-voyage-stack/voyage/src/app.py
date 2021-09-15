"""
Ce programme permet la gestion des voyages
"""
from flask import Flask, request
import repository

app = Flask(__name__)

@app.route("/voyages/<id>", methods=["GET"])
def trouver_voyage_par_id(id):
    return repository.trouver_voyage_par_id(id)

@app.route("/voyages", methods=["GET"])
def trouver_tout_voyages():
    voyages = repository.trouver_tout_voyages()
    return {"results":voyages}

@app.route("/voyages", methods=["POST"])
def sauvegarder_voyage():
    voyage = request.json
    return repository.sauvegarder_voyage(voyage)

if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")