#!/usr/bin/env python3
"""Session Auth class"""
from api.v1.auth.session_auth import SessionAuth
import os
import datetime


class SessionExpAuth(SessionAuth):
    """ Session Ext Auth class"""
    def __init__(self):
        """ Constructor method"""
        if os.getenv('SESSION_DURATION'):
           self.session_duration = int(os.getenv('SESSION_DURATION'))
        else:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Create session method"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        SessionAuth.user_id_by_session_id[session_id] = {
            'user_id': user_id, 'create_at': datetime.now()}
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ User id for session method"""
        if session_id is None:
            return None
        if not user_id_by_session_id[session_id]:
            return None
        if self.session_duration <= 0:
            return SessionAuth.user_id_by_session_id[session_id].user_id
        if not user_id_by_session_id.has_key('created_at'):
            return None
        return SessionAuth.user_id_by_session_id[session_id].user_id

