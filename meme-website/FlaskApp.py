#!/bin/python
import os
from flask import Flask, render_template
#render_template allows us to reference external https tempplates
import requests
import json
app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_meme():
    url = os.getenv('MEME_API_URL')
    response = requests.get(url)
    data = response.json()
    meme_pic = data["preview"][-2]
    subreddit = data["subreddit"]

    return render_template("meme-index.html", meme_pic = meme_pic, subreddit=subreddit)

app.run(host="0.0.0.0", port=5001, debug=True)