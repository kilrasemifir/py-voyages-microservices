"""
Microservice en python pour la creation de ticket de cinema.
Ce microservice permet:
- la creation d'un ticket de cinema en fonction de son id
"""


from flask import Flask
from os import environ
from requests import get
from datetime import date
cinema_port = environ.get("CINEMA_PORT", 80)
cinema_host = environ.get("CINEMA_HOST", "localhost")

app = Flask("cinema")

@app.route("/<id>", methods=["GET"])
def trouver_tous_cinemas(id):
    request_result = get(f"http://{cinema_host}:{cinema_port}/{id}")
    cinema = request_result.json()
    return f"""
nom du cinema: {cinema["nom"]}
date         : {date.today()}
    """

app.run(port=int(environ.get("PORT", 80)))
