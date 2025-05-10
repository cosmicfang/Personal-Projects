#!bin/python

from flask import FLask

app = Flask(__name__)

@app.route("/")

def index():
    return "Drink more CHAIII!!!!"


app.run(host="0.0.0.0", port=5000)
