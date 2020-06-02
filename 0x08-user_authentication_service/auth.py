#!/usr/bin/env python3
""" Auth module"""
import bcrypt
from typing import ByteString


def _hash_password(password: str) -> str:
    """ method that takes in a password
        string arguments and returns a string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
