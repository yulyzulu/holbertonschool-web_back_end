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
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Method that return User ID based on a Session ID"""
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Instance Method that returns a User instance based on
            a cookie value"""
        session_id = self.session_cookie(request)
        user = self.user_id_for_session_id(session_id)
        return User.get(user)

    def destroy_session(self, request=None):
        """ Method that deletes the user session / logout"""
        if request is None:
            return False
        if not self.session_cookie(request):
            return False
        session_id = self.session_cookie(request)
        if not self.user_id_for_session_id(session_id):
            return False
        self.user_id_by_session_id.pop(session_id)
        return True
