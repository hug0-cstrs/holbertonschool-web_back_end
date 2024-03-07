#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)

babel = Babel(app)
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'


@app.route('/', methods=['GET'])
def hello():
    """ GET /
    Return:
      Render template
    """
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
