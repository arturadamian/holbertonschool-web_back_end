#!/usr/bin/env python3
""" API authentication
"""
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar


class SessionAuth(Auth):
    """ Session Auth class"""
