#!/usr/bin/env python3
""" API authentication
"""
from api.v1.auth.session_auth import SessionAuth
from flask import request
from typing import List, TypeVar
from datetime import datetime, timedelta
import uuid
from models.user import User
from os import getenv


class SessionExpAuth(SessionAuth):
    """ Session Exp Auth class"""
    def __init__(self):
        """Constructor"""
        if getenv('SESSION_DURATION'):
            session_duration = int(getenv('SESSION_DURATION'))
        else:
            session_duration = 0

    def create_session(self, user_id=None):
        """Create a Session ID by calling super()"""
        session_id = super().create_session(user_id)
        if not session_id:
            return
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if not session_dictionary:
            return
        session_dictionary['user_id'] = user_id
        session_dictionary['created_at'] = datetime.now()
        return session_dictionary

    def user_id_for_session_id(self, session_id=None):
        """Overload """
        if not session_id:
            return
        session_dictionary = self.user_id_by_session_id.get("session_id")
        if not session_dictionary:
            return
        if self.session_duration <= 0:
            return session_dictionary['user_id']
        if not session_dictionary.get('created_at'):
            return
