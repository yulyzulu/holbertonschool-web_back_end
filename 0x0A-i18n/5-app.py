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
    locale = request.args.get("locale")
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello():
    """Greet function"""
    return render_template('5-index.html')

def get_user():
    """Function to get user"""
    login_as = request.args.get("login_as")
    if login_as:
        return users[login_as]
    else:
        return None

@app.before_request
def before_request():
    """Before request function"""
    g.user = get_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
