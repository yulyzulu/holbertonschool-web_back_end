#!/usr/bin/env python3
""" Auth class"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic Auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Method that returns the Base64 parth of the Authorization
            header"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header.split()[0] == "Basic":
            return authorization_header.split()[1]
        else:
            return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
        """Method that returns the decoded value of a Base64"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            message_bytes = base64.b64decode(base64_authorization_header)
            message = message_bytes.decode('utf-8')
            return message
        except Exception:
            return None
