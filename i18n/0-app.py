#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def hello():
    """ GET /
    Return:
      - Render template
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
