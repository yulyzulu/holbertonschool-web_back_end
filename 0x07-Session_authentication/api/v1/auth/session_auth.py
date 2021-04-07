#!/usr/bin/env python3
"""Session Auth class"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User
import uuid


class SessionAuth(Auth):
    """ Session Auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Method that creates a Session ID for a user_id"""
        if user_id is None or type(user_id) is not str:
            return None
        id = uuid.uuid4()
        self.user_id_by_session_id[id] = user_id
        return id
