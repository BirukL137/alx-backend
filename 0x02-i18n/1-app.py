#!/usr/bin/env python3
"""
Basic Babel setup
"""

from flask_babel import Babel
from flask import Flask, render_template


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
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
