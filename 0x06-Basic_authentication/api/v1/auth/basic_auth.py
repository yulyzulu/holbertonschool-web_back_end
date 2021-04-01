#!/usr/bin/env python3
""" Auth class"""
from  api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Auth class"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Method that returns the Base64 parth of the Authorization header"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header.split()[0] == "Basic":
            return authorization_header.split()[1]
        else:
            return None
