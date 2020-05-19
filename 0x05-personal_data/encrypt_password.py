#!/usr/bin/env python3
""" User passwords should NEVER
    be stored in plain text in a database
"""
import bcrypt


def hash_password(pw: str) -> bytes:
    """returns a salted, hashed password, which is a byte string"""
    return bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
