#!/usr/bin/env python3
""" Auth class"""

from flask import request
from typing import List, TypeVar
import os


class Auth:
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth public method that returns False - path and
             excluded_paths"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if path[-1] != '/':
            path = path + '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ Authorization_header that returns None - request"""
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user method"""
        return None

    def session_cookie(self, request=None):
        """Method that returns a cookie value from request"""
        if request is None:
            return None
        cookie = os.environ.get('SESSION_NAME')
        cookie_value = request.cookies.get(cookie)
        return cookie_value
