#!/usr/bin/env python3
"""
Force locale with URL parameter
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
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """
    This function is invoked for each request to select a language
    translation to use for that request.
    """
    lcl = request.args.get('locale')
    if lcl in app.config['LANGUAGES']:
        return lcl
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
