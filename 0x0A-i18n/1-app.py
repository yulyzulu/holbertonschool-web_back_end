#!/usr/bin/env python3
""" App file """

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class"""
    LANGUAGES = ["en", "fr"]

app.config.from_object(Config)
Babel.default_locale = "en"
Babel.default_timezone = "UTC"


@app.route('/')
def hello() -> str:
    """Greet function"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
