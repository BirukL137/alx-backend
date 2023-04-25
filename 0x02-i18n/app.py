#!/usr/bin/env python3
"""
Display the current time
"""

from flask_babel import Babel
from flask import Flask, render_template, request, g
from pytz import timezone
import pytz.exceptions

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    "A Config class"
    LANGUAGES = ["en", "fr"]
    DEBUG = True
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """ Returns a user id. """
    id = request.args.get('login_as')
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """ Add a user """
    user = get_user()
    g.user = user


@app.route('/')
def index():
    """ Returns the index page. """
    return render_template('7-index.html')


@babel.localeselector
def get_locale():
    """
    This function is invoked for each request to select a language
    translation to use for that request.
    """
    lcl = request.args.get('locale')
    if lcl in app.config['LANGUAGES']:
        return lcl

    if g.user:
        lcl = g.user.get('locale')
        if lcl and lcl in app.config['LANGUAGES']:
            return lcl

    lcl = request.headers.get('locale')
    if lcl in app.config['LANGUAGES']:
        return lcl
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Return appropriate timezone
    """
    time_zone = request.args.get('timezone', None)
    if time_zone:
        try:
            return timezone(time_zone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        try:
            time_zone = g.user.get('timezone')
            return timezone(time_zone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == "__main__":
    app.run()
