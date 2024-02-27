#!/usr/bin/env python3
""" Main file
"""

from auth import Auth
from flask import Flask, abort, jsonify, request

app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def welcome():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie('session_id', session_id)
            return response
        else:
            abort(401)
    except ValueError:
        abort(401)

@app.route('/sessions', methods=['POST'])
def login():
    """ POST /sessions """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie('session_id', session_id)
            return response
        else:
            abort(401)
    except ValueError:
        abort(401)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
