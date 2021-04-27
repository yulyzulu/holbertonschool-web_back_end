#!/usr/bin/env python3
""" App file """

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Configuration class"""
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = "en"
Babel.default_timezone = "UTC"


def get_user() -> Union[dict, None]:
    """Function to get user"""
    try:
        login_as = request.args.get("login_as")
        return users[int(login_as)]
    except Exception:
        return None


@app.before_request
def before_request():
    """Before request function"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Get locale function"""
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello() -> str:
    """Greet function"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
