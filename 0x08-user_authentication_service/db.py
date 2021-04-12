#!/usr/bin/env python3
"""
Database file
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class"""

    def __init__(self):
        """ Constructor method"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Private property and hence should NEVER be used from outside
           the DB class"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add user method require email and hashed_password as
           argumetns and return a User object"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find user method takes in arbitrary keyword arguments and
           returns the first row found in the users table as filtered
           by the methods input arguments """
        keywords = ['id', 'email', 'hashed_password',
                    'session_id', 'reset_token']
        for i in kwargs.keys():
            if i not in keywords:
                raise InvalidRequestError
        data = self._session.query(User).filter_by(**kwargs).first()
        if data:
            return data
        else:
            raise NoResultFound

    def update_user(self, user_id: int, **kwargs)-> None:
        """Method that takes as argument a required user_id integer
            and arbitrary keyword arguments, and returns None"""
        keywords = ['id', 'email', 'hashed_password',
                    'session_id', 'reset_token']
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key in keywords:
                setattr(user, key, value)
            else:
                raise ValueError
        self._session.commit()
