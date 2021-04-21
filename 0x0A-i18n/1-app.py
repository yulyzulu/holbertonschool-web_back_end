#!/usr/bin/env python3
""" App file """

from flask import Flask, render_template, request
from flask_babel import Babel


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

@app.route('/')
def hello():
    """Greet function"""
    return render_template('1-index.html', locale=get_locale() or babel.default_locale)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
