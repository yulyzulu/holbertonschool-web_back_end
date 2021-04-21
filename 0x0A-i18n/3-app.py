#!/usr/bin/env python3
""" App file """

from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    LANGUAGES = ["en", "fr"]

app.Config['BABEL_DEFAULT_LOCALE'] = 'en'
app.Config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@babel.localeselector
def get_locale():
    """Get locale function"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

home_title = flash(_("Welcome to Holberton"))
home_header = flask(_("Hello world!"))

@app.route('/')
def hello():
    """Greet function"""
    return render_template('3-index.html', locale=get_locale(), home_title=home_title, home_header=home_header)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
