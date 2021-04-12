#!/usr/bin/env python3
"""
App file
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def welcome():
    return flask.jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
