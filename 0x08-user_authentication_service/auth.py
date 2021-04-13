#!/usr/bin/env python3
"""
Auth file
"""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """Hash password method that return a salted hash of the input
       password"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def _generate_uuid() -> str:
    """The function should return a string representation of a new UUID"""
    id = str(uuid.uuid4())
    return id

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Constructor method"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register method"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email=email, hashed_password=hashed_pwd)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Method that valid login"""
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
        except NoResultFound:
            return False
