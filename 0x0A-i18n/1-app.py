#!/usr/bin/env python3
""" App file """

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]


#app.Config['BABEL_DEFAULT_LOCALE'] = "en"
#app.Config['BABEL_DEFAULT_TIMEZONE'] = "UTC"


@app.route('/')
def hello():
    """Greet function"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
