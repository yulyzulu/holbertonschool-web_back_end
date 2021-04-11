#!/usr/bin/env python3
""" User model """

#from sqlalchemy import Column, Integer, String

User.__table__
Table('users', MetaData(bind=None),
            Column('id', Integer(), primary_key=True),
            Column('email', String(), nullable=False),
            Column('hashed_password', String(), nullable=False),
            Column('session_id', String(), nullable=True),
            Column('reset_token', String(), nullable=True), schema=None)
