#!/usr/bin/env python3
""" User passwords should NEVER
    be stored in plain text in a database
"""
import bcrypt


def hash_password(pw: str) -> bytes:
    """returns a salted, hashed password, which is a byte string"""
    return bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())


def is_valid(h_password: bytes, password: str) -> bool:
    """validates that the provided password matches the hashed password
    """
    return bcrypt.checkpw(password.encode('utf-8'), h_password)
