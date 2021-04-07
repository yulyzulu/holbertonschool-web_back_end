#!/usr/bin/env python3
""" Auth class"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


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
                                           base64_authorization_header: str
                                           ) -> str:
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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ Method that returns the user email and password from the
            Base64 decode value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        decoded_header = decoded_base64_authorization_header.split(':')
        if len(decoded_header) >= 2:
            pwd = decoded_header[1]
            if len(decoded_header) > 2:
                print(len(decoded_header))
                for i in range(1, len(decoded_header) - 1):
                    pwd += decoded_header[i + 1]
            return decoded_header[0], pwd
        else:
            return None, None

    def user_object_from_credentials(self, user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """Method that returns the User instance based on his email
           and password"""
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        users = User.search({'email': user_email})
        if not users:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
            else:
                return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method that overloads Auth and retrieves the User instance
           for a request"""
        try:
            header = self.authorization_header(request)
            encode = self.extract_base64_authorization_header(header)
            decode = self.decode_base64_authorization_header(encode)
            user, pwd = self.extract_user_credentials(decode)
            user_obj = self.user_object_from_credentials(user, pwd)
            return user_obj
        except Exception:
            return None
