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

    def create_session(self, email: str) -> str:
        """ Create session method, return the Session Id"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Get user by session id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Method that destroy the session """
        try:
            self._db.update_user(user_id, session_id=None)
            return None
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Method that reset password token"""
        try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Update password method """
        if reset_token is None or password is None:
            return None
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_pwd = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_pwd,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError
