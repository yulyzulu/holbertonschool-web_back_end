#!/usr/bin/env python3
""" Auth class"""

from flask import request


class Auth():
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth public method that returns False - path and
             excluded_paths"""
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization_header that returns None - request"""
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """Current user method"""
        return None
