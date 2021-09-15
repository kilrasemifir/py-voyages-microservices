"""
Ce programme permet la gestion des tickets
"""
from flask import Flask
from os import environ
import requests as http

VOYAGE_HOST = environ.get("VOYAGE_HOST", "localhost")
VOYAGE_PORT = int(environ.get("VOYAGE_PORT", 8080))
SERVER_PORT = int(environ.get("SERVER_PORT", 8080))

app = Flask(__name__)

@app.route("/tickets", methods=["GET"])
def tickets_avec_tout_voyages():
    http_response = http.get(f"http://{VOYAGE_HOST}:{VOYAGE_PORT}/voyages")
    http_body = http_response.json()
    voyages = http_body["results"]
    ticket = ""
    for voyage in voyages:
        ticket += f"""
        <div>
            <span><b>Voyage:</b> {voyage["titre"]}</span>
            <span><b>description:</b> {voyage["description"]}</span>
        </div>
        ***********************************
        """ 
    return ticket

if __name__ == "__main__":
    app.run(port=SERVER_PORT, host="0.0.0.0")