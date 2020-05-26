#!/usr/bin/env python3
""" API authentication
"""
from flask import request
from typing import List, TypeVar


class SessionAuth(Auth):
    """ manages the API authentication"""
    self.issubclass(SessionAuth, Auth)