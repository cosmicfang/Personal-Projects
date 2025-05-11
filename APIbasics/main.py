#!/bin/python

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# I need to create a dict to simulate a db in memory and reimplement this


@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id" : user_id,
        "name" : "john.doe",
        "email" : "john.doe@example.com"
    }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST", "GET"])
def create_user():
    if request.method == "POST":
        data = request.get_json()
        return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)