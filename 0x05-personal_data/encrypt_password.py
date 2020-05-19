#!/usr/bin/env python3
import bcrypt


def hash_password(pw: str) -> bytes:
    """returns a salted, hashed password, which is a byte string"""
    hashed = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
    return hashed
