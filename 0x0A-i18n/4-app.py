#!/usr/bin/env python3
""" App file """

from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class"""
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = "en"
Babel.default_timezone = "UTC"


@babel.localeselector
def get_locale() -> str:
    """Get locale function"""
    #return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'fr'


@app.route('/')
def hello():
    """Greet function"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
