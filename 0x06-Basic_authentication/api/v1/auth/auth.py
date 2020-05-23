#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar


class Auth():
    """manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authorithation"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1:] != '/':
            path += '/'
        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if request is None or 'Authorization' not in request.headers:
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
