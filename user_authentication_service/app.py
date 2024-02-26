#!/usr/bin/env python3
""" Main file
"""

<<<<<<< HEAD
from auth import Auth
from flask import Flask, jsonify, request

app = Flask(__name__)
AUTH = Auth()
=======
from flask import Flask, jsonify

app = Flask(__name__)
>>>>>>> 03d642334312b0705d6b88ba6464d9d93106e684


@app.route('/')
def welcome():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

