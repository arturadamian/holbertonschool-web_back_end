#!/usr/bin/env python3
import bcrypt


def hash_password(pw: str) -> bytes:
    """returns a salted, hashed password, which is a byte string"""
    password = b"super secret password"
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed
