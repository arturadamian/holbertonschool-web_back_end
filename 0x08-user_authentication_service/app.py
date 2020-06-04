#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def hello() -> str:
    """welcome msg"""
    return jsonify({"message": "Bienvenue"})


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """registering the user"""
    email = request.form.get('email')
    # print(email)
    password = request.form.get('password')
    # print(password)
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": {email}, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app_views.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """respond to the POST /sessions route"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": {email}, "message": "logged in"})
    response.set_cookies('session_id', session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
