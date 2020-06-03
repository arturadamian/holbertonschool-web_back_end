#!/usr/bin/env python3
""" Auth module"""
import bcrypt
from db import DB
from typing import TypeVar


def _hash_password(password: str) -> str:
    """ method that takes in a password
        string arguments and returns a string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> TypeVar('User'):
        """ hash the password with _hash_password
            save the user to the database using self._db
            return the User object
        """
        user = DB.find_user_by(self, email=email)
        if user:
            raise ValueError('User {email} already exists')
        pd = _hash_password(password)
        self._db.add_user(email, pd)
