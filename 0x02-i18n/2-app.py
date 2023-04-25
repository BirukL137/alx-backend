#!/usr/bin/env python3
"""
Get locale from request
"""

from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    "A Config class"
    LANGUAGES = ["en", "fr"]
    DEBUG = True
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """ Returns the index page. """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """
    This function is invoked for each request to select a language
    translation to use for that request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
