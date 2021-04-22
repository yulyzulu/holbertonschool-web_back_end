#!/usr/bin/env python3
""" App file """

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class"""
    LANGUAGES = ["en", "fr"]

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@babel.localeselector
def get_locale():
    """Get locale function"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def hello():
    """Greet function"""
    return render_template('2-index.html', locale=get_locale())




if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
