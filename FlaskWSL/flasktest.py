#!/bin/python
from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
	return "Drink more CHAII bruhhhvvvvv"

app.run(host="0.0.0.0", port=5000)
